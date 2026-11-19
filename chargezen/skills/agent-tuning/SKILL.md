---
name: agent-tuning
description: Improve an existing Chargezen Concierge agent from what customers actually asked it — read recent conversations it handled and the ones it handed to the team, find where it struggled, then propose specific changes to its instructions, tools, channels or reply style, and save only the ones the merchant approves. Use when an agent hands over too often, gives wrong or vague answers, should handle something new, or they want it "smarter".
argument-hint: "<agent name> [what's wrong]"
---

# Agent tuning

The agent and the problem: $ARGUMENTS

Follow the `chargezen` skill for how to reach the tools. **Read only** until the person approves a change.

## 1. Read the agent

1. `chargezen.agents.list.v1`, then `chargezen.agents.get.v1` on the one they named (ask if several match). Note its role, status, instructions, `tool_names`, channels (`channel_endpoint_ids`), `channel_response` and `updated_at`.
2. `chargezen.agents.configuration_options.v1`: the tools it could have (`tools`, with the roles each works for and the tools it needs) and the workspace's channels.

## 2. See how it's doing

Look at the last 14 days unless they gave a period.

1. **Handed to the team:** `chargezen.inbox.list.v1` with `status: "handoff_queue"`, then `status: "all"` filtered by the agent's channels. Read a sample of handed-over conversations with `chargezen.inbox.get.v1` (up to ten). For each, note what the customer wanted and why the agent couldn't finish: it lacked a tool, the knowledge didn't say, its instructions told it to stop, or the customer asked for a person.
2. **What it said:** `chargezen.history.search.v1` with `since` set to the period, for the topics the person raised or that came up above (for example "refund", "where is my order", "cancel", "discount code"). Read around a match with `chargezen.history.read.v1` when the fragment isn't enough. Messages with `sender: "agent"` are the agent's answers; check the facts they state against knowledge (`chargezen.knowledge.search.v1`) or orders (`chargezen.admin_shopify_orders.search.v1`) rather than trusting them.
3. **Knowledge it lacked:** for each question it couldn't answer, `chargezen.knowledge.search.v1`. If nothing answers it, the fix is knowledge, not instructions: offer `/knowledge-gaps`.

Search results show the best matches, not every one; say "seen in N of the conversations read", never a total.

## 3. Propose changes

Up to five, ranked by how many customers each would help. Each one line: what happens now (with one real example, customer name left out), the change, and what it lets the agent do. Typical ones:

- **Instructions:** a clearer rule for when to hand over, a step it skips (signing customers in before account details), a tone fix, a topic it should decline.
- **Tools:** a capability it lacks, chosen from `tools` with its role, plus everything that tool lists in `required_tool_names`. Name any that change an order, subscription or money.
- **Reply style:** a channel's `format` or `max_characters` (texts too long, emails too short).
- **Channels:** a channel it should also answer, if it's in `channel_endpoints` and not held by another agent.

Show the new instructions in full, with the changed lines pointed out.

## 4. Save what they approve

`chargezen.agents.update.v1` with `expected_updated_at` set to the `updated_at` you read, and `changes` holding only the approved fields. A list you send replaces the whole field: send the complete `tool_names` (keeping the tools they want to keep), the complete `channel_endpoint_ids` (a channel left out is left with no agent), and every channel in `channel_response`. If the agent is active, the change applies to new messages right away; say so before saving. On `AGENT_CHANGED`, read it again with `chargezen.agents.get.v1`, show what someone else changed and redo the change on top.

## 5. Report

List what changed and what didn't, and suggest a check-in after a week of conversations.
