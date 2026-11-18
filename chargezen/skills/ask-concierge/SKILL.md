---
name: ask-concierge
description: Hand a job to Concierge, the merchant's Chargezen agent (also called Finn), and see it through — send the request with every detail it needs, wait for the answer, relay each approval request or question to the merchant in plain words, and pass their answer back in the same conversation. Use when a job is bigger than a lookup or needs a change this connection can't make directly, such as cancelling or returning an order, changing a subscription or customer, or multi-step work across tools.
argument-hint: "<the job, in your words>"
---

# Ask Concierge

The job: $ARGUMENTS

Follow the `chargezen` skill for how to reach the tools.

## 1. Decide whether Concierge is needed

Answer it yourself when the direct reads cover it: orders, shipping, stock and sales reports, knowledge, the inbox, past conversations and loyalty points. Those are free and faster.

Hand it to Concierge when it needs something this connection can't do directly, for example cancelling an order, starting a return, changing a subscription or a customer, or a long job across several tools. Concierge's work spends the workspace's Finn credits, so say so before the first request.

## 2. Write the request

`concierge.ask` with a `message` that stands on its own: who (customer name and email or order number), what to do, any limits ("refund shipping only", "don't email the customer"), and what to report back. Concierge doesn't see this chat, so include every fact it needs.

Chargezen asks the person to confirm each message before Concierge acts on it, unless they chose to always allow it. If the result is `CONFIRMATION_REQUIRED`, show them the message, and repeat the identical call with its `confirmation_token` only after they agree.

Keep the `conversation_ref` and `message_ref` from the result.

## 3. Follow it

The result's `status` says where it stands:

- **working:** no reply yet. Check with `concierge.get_reply` and the `message_ref`. Wait a little between checks; a long job can take minutes. Tell the person it's still working rather than guessing what it will say.
- **needs_input:** Concierge wants an approval or an answer. Show the person exactly what it asks, in plain words (what will change, for whom, what it costs), and wait for their answer. Never approve on their behalf.
- **replied:** Concierge has finished. `reply` is its answer.

To answer a question or an approval request, call `concierge.ask` again with the person's answer in their words and the same `conversation_ref`. Each call sends a new message (an identical call within two minutes returns the first result instead).

## 4. Report

Lead with what Concierge did or found, then anything it couldn't do and why. Numbers and changes come from its reply; don't add any of your own. The whole exchange also appears in the person's Chargezen admin inbox.

## When it can't run

- **No active Concierge agent** for this connection (`AGENT_UNAVAILABLE`): a workspace owner needs to turn that agent on in Chargezen. Say so and stop.
- **No credits left** (`CREDITS_EXHAUSTED`): give the person the link from the result to add credits. Don't retry.
- **A conversation or message isn't found:** start a new request without the old reference.
