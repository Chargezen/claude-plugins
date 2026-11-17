---
name: campaign
description: Build a one-off SmartyTap email, text or WhatsApp campaign in Chargezen from a short brief — audience, words and send time — as a draft, then check what's missing, count who gets it and what texts cost, send the merchant a test, and launch only when they say so. Use for a promotion, launch, announcement or newsletter to a list or segment.
argument-hint: "<what it's about, who gets it, when>"
---

# Campaign

The brief: $ARGUMENTS

Follow the `chargezen` skill for how to reach the tools. A campaign is a one-off send. For messages that repeat on an event (welcome, abandoned cart, win-back), say so and offer a flow instead.

## 1. Pin down the brief

Read `smartytap_campaigns.authoring_options` first: lists and segments, senders, the store's time zone, personalization, whether texts can send yet, and the brand (styles, images, templates).

From the brief and that, settle four things, asking only for what's missing, in one message:

- **Audience:** a list or segment by name. If none fits, offer to build a segment (`smartytap_segments.fields`, then `smartytap_segments.preview` to count it, then `save` on their OK).
- **Channel:** email, text, WhatsApp, or a mix. If texts aren't ready, say what setup step the options name and suggest email.
- **Send time:** now or a local time; times are in the store's time zone.
- **The offer and the one action** you want people to take.

Look at past results before you write: `smartytap_campaigns.list` with `status: "completed"`, then `report` on the two or three most recent, to reuse what got clicks.

## 2. Draft it

1. `smartytap_campaigns.create` with a new `operation_id`. Start the email from a fitting template or starter design named in the options.
2. Write the email at the document address the result gives, with `email_documents.apply_ops`: a subject under 50 characters, preview text that adds to it, one clear headline, short body, one button, the unsubscribe link and mailing address. Use personalization tokens exactly as the options list them.
3. Texts: under 160 characters where you can (each part costs credits), the store name first, one link, and the opt-out wording the workspace uses.
4. Offer a subject-line A/B test (`add_versions`) when the list is large enough to learn from.

## 3. Check it

- `smartytap_campaigns.review`: fix everything it lists before going on.
- `smartytap_campaigns.preview` to read the email as customers will.
- `smartytap_campaigns.preview_audience`: how many people can receive each message, and for texts the estimated credit cost against the balance.

Show the person: subject and preview text, a short summary of the body, who gets it (with the count), when it sends, and what texts cost.

## 4. Test, then launch

- On their OK, `send_test` to them (new `operation_id`).
- Launch only when they say to: `smartytap_campaigns.launch` confirms the recipients, text cost and revision you just showed; if any of those changed, show the new figures and ask again.
- After it sends, offer to read the results with `report` the next day.
