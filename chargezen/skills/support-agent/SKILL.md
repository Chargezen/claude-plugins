---
name: support-agent
description: Set up a customer-facing support agent in Chargezen Concierge — a digital employee that answers customers on web chat, checkout chat, text, WhatsApp, email or phone — with its name, instructions, the tools it may use and the channels it answers, saved as a draft and turned on only when the merchant says so. Use when they want an AI agent to answer customers, cover a channel after hours, or take order, shipping, subscription or loyalty questions.
argument-hint: "[channels, what it should handle]"
---

# Support agent

The request: $ARGUMENTS

Follow the `chargezen` skill for how to reach the tools. Saving an agent needs a teammate role that can manage Concierge conversations; if a call says access is missing, say so and stop.

## 1. See what's there

1. `agents.list`: the agents that already exist, their role, status and how many channels each answers. If a customer agent already covers what they want, offer to change it with `/agent-tuning` instead of adding a second one.
2. `agents.configuration_options`: the real choices for this workspace:
   - `roles`: `customer_agent` talks to customers; `operator_agent` works for the team. A support agent is a `customer_agent`.
   - `channel_endpoints`: the channels this workspace already has (web chat, checkout chat, mailboxes, phone numbers, WhatsApp), and which agent each is assigned to. This tool can't add a channel or take one over from another agent: a channel the workspace doesn't have yet, or one another agent holds, has to be set up or released in Chargezen first.
   - `tools`: each capability by name, the roles it works for and the other tools it needs (`required_tool_names`).
   - `model_sources` and `voice_speech_sources`: Chargezen managed, or the workspace's own provider account if one is connected.
   - `defaults` and `new_agent_id` (keep that ID for this one agent).

## 2. Agree the plan

Ask what they want only where it isn't clear, then propose:

1. **Name and display name**, the name customers see.
2. **Channels:** which of the existing, unassigned channels it answers.
3. **What it handles**, as tools picked only from `tools` with `customer_agent` in their roles. A sensible start, using whichever of these the list offers:
   - answers from the store's knowledge: `knowledge.search`, `knowledge.read`;
   - order status and tracking: `shopify_orders.list`, `get`, `get_tracking`, `shopify_fulfillment_orders.list_for_order`, and `shopify_shipping_zones.list` for "do you ship to";
   - products: `products.search`;
   - signing customers in before private account details: `customer.authenticate`;
   - handing over to a person: `conversations.request_handoff`.
   Add subscription changes (`customer_subscriptions.*`), loyalty (`customer_rewards.*`), returns or cancellations only when they ask. Name each one that changes an order, a subscription or money, and what the customer could do with it. Include every tool a chosen tool lists in `required_tool_names`; a save without them is refused.
4. **Instructions:** complete operating instructions in the store's voice: who it is, what it helps with, what it must not do (promise refunds, invent policies, discuss other customers), when to hand over to a person, and to sign customers in before account details. Ground facts in knowledge rather than writing policies into the instructions; if knowledge is thin, suggest `/knowledge-gaps` first.
5. **Reply style per channel** (`channel_response`, one entry per chosen channel kind): a `format` and `max_characters`. Texts short (around 300 characters), chat a few sentences, email a full reply; WhatsApp can't exceed the limit `channel_response_limits` gives. **Phone** also needs `speech`: language, whose speech account (`stt`, `tts` from `voice_speech_sources`), the opening lines for known, unknown and hidden callers, acknowledgment and keep-alive phrases and their timings. Read each field's description from the contract and write the exact words they'll hear.
6. **Model:** `model_routes` from `model_sources` (Chargezen managed unless they chose their own provider), `repair_plan_limit` from `defaults`.

Show the plan as a short summary: what customers will see, which channels, what it can and can't do.

## 3. Save it as a draft

`agents.create` with `agent_id` set to `new_agent_id` and the complete configuration, `status: "draft"`. A draft answers nobody. On a retry, keep the same `agent_id`; a repeat returns the existing agent instead of making another. If it's refused (`AGENT_CONFIGURATION_INVALID`, `AGENT_CHANNEL_UNAVAILABLE`), explain the reason in plain words, fix it and try again.

## 4. Turn it on only when they say so

Ask in one sentence: "Turn on <name>? From then on it answers new messages on <channels>." On a yes, `agents.update` with the `updated_at` from the save as `expected_updated_at` and `changes: { status: "active" }`. If the result is `AGENT_CHANGED`, read it again with `agents.get` and show what changed before trying again.

## 5. Report

Say what was saved, whether it's live, which channels it answers and what it can do. Suggest testing it with a real question on one channel, and `/agent-health` in a week.
