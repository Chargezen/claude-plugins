---
name: agent-health
description: A read-only check of every Concierge agent in the merchant's Chargezen workspace — which are live, which are drafts never turned on, channels that aren't ready or that nobody answers, agents with no channels or instructions, tools that need a missing companion or don't fit the agent's role, phone agents without speech settings, whether anyone is alerted when a customer asks for a person, and customers waiting in the handoff queue — ending with a ranked list of fixes. Use when they ask whether their agents are set up right, which channels are covered, or before going live.
argument-hint: "[agent name, or all]"
---

# Agent health check

Check: $ARGUMENTS (every agent if nothing was named).

Follow the `chargezen` skill for how to reach the tools. **Read only** until the person picks a fix.

## 1. Gather

1. `chargezen.agents.list.v1`: every agent's name, role, status, tools and channel count.
2. `chargezen.agents.configuration_options.v1`: the workspace's channels (`channel_endpoints`, with which agent each is assigned to and whether the channel is active), the tools each role can use (`tools`, with `agent_roles` and `required_tool_names`), and `channel_response_limits`.
3. `chargezen.agents.get.v1` for each agent that isn't archived: its instructions, tools, channels, reply style per channel and model.
4. `chargezen.inbox.list.v1` with `status: "handoff_queue"`: customers waiting for a teammate after an agent handed over, longest waiting first.
5. `chargezen.channels.list.v1`: each customer channel (web chat, checkout chat, texts, email, WhatsApp, phone), whether it's ready, why not and the next step.
6. `chargezen.support_settings.get.v1`: business hours and who is alerted when a customer asks for a person.

These tools don't report how many conversations an agent answered or how well. Say so rather than guessing; offer `/agent-tuning` to read real conversations.

## 2. What to flag

- **Channels nobody answers:** an active channel in `channel_endpoints` with no `assigned_agent_id`, or assigned to an agent that is a draft or disabled. Customers there get no agent reply.
- **Live but empty:** an active agent with no channels, or with no or very short instructions.
- **Drafts left behind:** a finished-looking draft that was never turned on, especially one with channels assigned.
- **Tools that don't fit:** a tool whose `agent_roles` don't include the agent's role, a tool missing something it lists in `required_tool_names`, or a tool name no longer offered in `tools`.
- **Risky grants on a customer agent:** tools that cancel orders, create returns or cancel subscriptions. Not wrong, but confirm they're intended.
- **Missing basics on a customer agent:** no knowledge search, no way to hand over to a person (`conversations.request_handoff`), or private account tools without `customer.authenticate`.
- **Reply style gaps:** a channel the agent answers with no `channel_response` entry, texts with a high `max_characters`, or a phone channel without speech settings (language, opening lines).
- **Overlap:** two active customer agents with near-identical instructions.
- **Channels not ready:** a channel `chargezen.channels.list.v1` shows as needing setup, pending, turned off or needing an agent, with its plain reason.
- **Nobody alerted:** no teammate gets an email or text alert when a customer asks for a person, or no business hours saved while the team clearly keeps them.
- **Waiting customers:** how many are in the handoff queue and the oldest wait.

## 3. Report

Lead with the three fixes that matter most, each one line: the agent or channel, what's wrong, what it costs (customers unanswered, a risky permission) and the fix. Then one line per agent: name, live or draft, channels, and "looks fine" or the issue. No tables longer than ten rows.

Offer to fix what they choose: change an agent with `/agent-tuning`, build a missing one with `/support-agent`, finish a channel or set the hours and handoff alerts with `/channel-setup`, or work the waiting customers with `/inbox-triage`. Turning an agent on or off, or moving a channel, changes who answers customers from that moment: say so and wait for a yes.
