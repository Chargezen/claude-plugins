---
name: direct-message
description: Write one person a one-to-one text or email from the store's number or mailbox in Chargezen SmartyTap — find them (or their company), save them as a contact if they're new, draft the message for the merchant to approve, then send it now or schedule a text for later. Use for "text Jamie that her order is ready", following up with a wholesale buyer, or writing to someone at a company. Not for messaging many people, which is a campaign.
argument-hint: "<who> <what to say> [text or email, when]"
---

# Direct message

The request: $ARGUMENTS

Follow the `chargezen` skill for how to reach the tools. A one-to-one message is for one person (or a handful). For more, say so and offer `/campaign`: a one-to-one message never replaces one, and is never marketing.

## 1. Find the person

1. `contacts.search` by name, email or phone. For someone at a business, `companies.search`, then `companies.get` (it also shows the latest conversation with anyone there) and `contacts.search` with that `company_id`.
2. `contacts.get` on the right person: their phones and emails, consent per channel, language, and their existing conversations. If they've already been talking to the team, offer to reply in that conversation (`inbox.get`, then `inbox.reply`) so the thread stays together.
3. Nobody found? Ask the merchant to confirm the details, then save them with `contacts.create` (add `also_in_shopify` only if they want a store customer too; that makes or reuses one tagged `smarty_tap_contact`). Saving someone sends them nothing and doesn't sign them up for marketing. If the merchant says the person agreed to marketing, record it with `contacts.record_consent`.

## 2. Draft it

- **Text:** short, from the store's voice, one link at most. Someone who replied STOP or is on the do-not-text list can't be texted; say so and offer email instead. Outside quiet hours a text is held until they end. Each text uses SMS credits.
- **Email:** a subject (needed when it starts a new thread) and a short, personal body.
- **From:** the usual number or the workspace's default mailbox, unless the merchant names one (`inbox.senders`).
- **Later:** a text can wait until a set time (`send_at`, in the store's time zone with its UTC offset). Email goes now.

Show the person who it goes to, from which number or mailbox, when, and the exact words.

## 3. Send on their OK

`inbox.compose` with a new `operation_id`, the channel, `contact_id` (or phone or email) and the approved words exactly. It joins their conversation on that channel or starts one. Add `assign_to_user_id` (from `inbox.assignable_teammates`) if a teammate should own the follow-up; they're notified. It can't be unsent.

Report what happened, including if the result says it wasn't sent (an opt-out) or is waiting (quiet hours or a scheduled time).
