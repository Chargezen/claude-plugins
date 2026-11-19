---
name: channel-setup
description: Get the ways customers reach a Chargezen workspace ready and answered — check every channel (storefront chat, checkout chat, texts, email, WhatsApp, phone calls), finish the setup of the ones the merchant wants, choose which agent answers each, and set business hours and who is alerted when a customer asks for a person — saying honestly which steps stay with the merchant, such as the theme app embed, the Meta sign-up, DNS records and carrier review. Nothing is bought, submitted to carriers, published, disconnected or released without an explicit OK on the exact item. Use when they want customers to reach them on a new channel, ask which channels are live, or a channel isn't working.
argument-hint: "[channels]"
---

# Channel setup

The request: $ARGUMENTS (every channel if nothing was named).

Follow the `chargezen` skill for how to reach the tools. **Read only** until the person approves a step.

## 1. Where every channel stands

1. `chargezen.channels.list.v1`: each customer channel, whether it's ready, why not in plain words, the next step, and each of its endpoints (a number, a mailbox, the web chat) with the agent assigned to it.
2. `chargezen.agents.list.v1`: the agents that exist and which are live.

Give one line per channel: ready, or what's missing. Ask which channels they want; don't push them to set up all of them.

## 2. Finish each channel they want

Follow the channel's `next_step`. In short, per channel:

**Storefront chat.** Design and publish the launcher with `/chat-launcher` (`chargezen.web_chat.get.v1`, `chargezen.web_chat.save.v1`, then `chargezen.web_chat.publish.v1` only on an explicit yes; publishing replaces what shoppers see and turns the web chat channel on). The merchant's step: turn on the **Concierge Widget** app embed in the Shopify theme editor.

**Checkout chat.** It's a CheckoutOS checkout widget (live chat): set it up with `/checkout-widgets`, which needs CheckoutOS.

**Texts.** `chargezen.smartytap_sms.get_setup.v1` lists what's left (`blockers`). A first number is toll-free and needs carrier verification:
1. Show and save the privacy policy address and the HELP, STOP and START replies (`chargezen.smartytap_sms.save_business_details.v1`; the replies apply at once), then the carriers' contact person and US business address (`chargezen.smartytap_sms.save_verification_contact.v1`).
2. `chargezen.smartytap_sms.search_numbers.v1` with `number_type: "toll_free"`; the merchant picks the number.
3. `chargezen.smartytap_sms.draft_toll_free_verification.v1`: show it in plain words, ask for a link to a screenshot of their sign-up form, take corrections.
4. Say the number is a **monthly cost** (no price is given, so quote none) and the verification goes to carriers as written. Only on an explicit OK on both: `chargezen.smartytap_sms.register_toll_free_number.v1`. Carrier review usually takes 3 to 5 business days.
Local (area-code) numbers also need local-texting registration: `chargezen.smartytap_sms.register_local_texting.v1` returns a payment link for the carrier fees that a teammate who may pay workspace bills opens in their own browser; never pay for them. Another number: `chargezen.smartytap_sms.search_numbers.v1`, then `chargezen.smartytap_sms.buy_number.v1` with the exact number they confirm.

**Email.** `chargezen.email_channel.list_mailboxes.v1` shows each mailbox and what holds it back.
- **A Google Workspace or Microsoft 365 mailbox they already have** (such as `support@brand.com`): `chargezen.email_channel.connect_external_mailbox.v1` returns a sign-in link. Give it to them: they sign in as that mailbox in their browser within 20 minutes. Then check `chargezen.email_channel.list_mailboxes.v1` again.
- **A mailbox at another provider** needs its password, so it's connected in Concierge's Third-party Email page, not here.
- **A mailbox Chargezen hosts on their own domain:** `chargezen.email_channel.add_domain.v1` with `sends: "mailbox"` on `reply.<their domain>`. List the DNS records it returns; adding them at their domain provider is the merchant's step. Then `chargezen.email_channel.check_domain.v1` (records can take up to an hour). Once the domain is ready, `chargezen.smartytap_senders.add_team_sender.v1` adds the team mailbox (such as `support@reply.brand.com`) with its From name; `chargezen.email_channel.list_mailboxes.v1` then shows it with the endpoint an agent answers it on. One teammate's personal mailbox is added in Concierge → Channels → Email.
- **A mailbox turned off:** `chargezen.email_channel.update_mailbox.v1` with `active: true`.

**WhatsApp.** `chargezen.whatsapp_channel.get.v1` gives the steps still needed. Connecting WhatsApp or adding a number is a Meta sign-up a teammate completes in their browser at `connect_url`; these tools can't do it. Afterwards, or after a change in WhatsApp Manager, `chargezen.whatsapp_channel.refresh.v1`. If a number shows its WhatsApp Business app history import pending, `chargezen.whatsapp_channel.retry_history_sync.v1` (Meta allows it only in the first 24 hours). Stopping one number (`chargezen.whatsapp_channel.deactivate_number.v1`) or all of WhatsApp (`chargezen.whatsapp_channel.disconnect.v1`) needs an explicit OK on exactly that, and turning it back on means the Meta sign-up again.

**Phone calls.** `chargezen.voice_channel.status.v1` shows each calling number, what blocks it and numbers the workspace already owns that could take calls.
1. Use an owned number (`chargezen.voice_channel.add_number.v1` with `purchase: false`), or a new one the merchant picks from `chargezen.voice_channel.search_numbers.v1` (`purchase: true`, a **monthly cost**, only on an explicit OK on that number).
2. It starts answering no calls. Assign its agent (step 3), then `chargezen.voice_channel.configure_number.v1` with `status: "active"` and who answers: the agent only, the agent first, teammates' Chargezen phone apps first (with how long they ring), or teammates only.
3. Recording: calls are recorded only after a notice callers hear. If they want recording, agree the notice (start from `suggested_notice` in the status) and save it with `chargezen.voice_channel.update_recording_policy.v1`.
Taking a number out of calling keeps it for texts (`chargezen.voice_channel.remove_number.v1`). Giving a number up for good (`chargezen.smartytap_sms.release_number.v1`) ends its texts and calls and may be permanent: only on an explicit OK on that exact number.

## 3. Choose who answers

Each endpoint in `chargezen.channels.list.v1` has a `channel_endpoint_id`.

- **An existing agent:** `chargezen.agents.get.v1` for its `channel_endpoint_ids` and `updated_at`, then `chargezen.agents.update.v1` with `expected_updated_at` and the **complete** list: the channels it already answers plus the new ones. A channel left out loses its agent.
- **A channel another agent holds:** take it out of that agent's list first, on the merchant's OK.
- **No suitable agent:** build one with `/support-agent`. A phone agent also needs its speech settings (greeting and voice), which that skill covers.

Ask first: "From now on <agent> answers new messages on <channel>. OK?" An agent answers only once it's active.

## 4. When nobody's around

`chargezen.support_settings.get.v1`, then propose what's missing: business hours, time zone and closed days (outside them, a customer who asks for a person is told when the team is back, and the launcher can show whether the team is available), which teammates get an email or a text when a customer asks for a person (from `chargezen.inbox.assignable_teammates.v1`; a text alert needs the teammate's phone saved in Chargezen), and auto-close for quiet conversations. These apply to the whole workspace: on their OK, `chargezen.support_settings.save.v1` with only the values that change.

## 5. Check and report

`chargezen.channels.list.v1` again. One line per channel: ready and who answers, or what's left. Then the steps waiting on the merchant or someone else, each with what to do: the app embed, the Meta sign-up, DNS records, a mailbox sign-in, a payment link, carrier review time. Offer `/agent-health` once the channels are live.
