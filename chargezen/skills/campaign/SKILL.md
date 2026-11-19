---
name: campaign
description: Build a one-off SmartyTap email, text or WhatsApp campaign in Chargezen from a short brief — audience, words and send time — as a draft, then check what's missing, count who gets it and what texts cost, send the merchant a test, and launch only when they say so. Use for a promotion, launch, announcement or newsletter to a list or segment.
argument-hint: "<what it's about, who gets it, when>"
---

# Campaign

The brief: $ARGUMENTS

Follow the `chargezen` skill for how to reach the tools. A campaign is a one-off send. For messages that repeat on an event (welcome, abandoned cart, win-back), say so and offer a flow instead.

## 1. Pin down the brief

Read `chargezen.smartytap_campaigns.authoring_options.v1` first: lists and segments, senders, the store's time zone, personalization, whether texts can send yet, and the brand (styles, images, templates).

From the brief and that, settle four things, asking only for what's missing, in one message:

- **Audience:** a list or segment by name. If none fits, offer to build a segment (`chargezen.smartytap_segments.fields.v1`, then `chargezen.smartytap_segments.preview.v1` to count it, then `chargezen.smartytap_segments.save.v2` on their OK).
- **Channel:** email, text, WhatsApp, or a mix. If texts aren't ready, say what setup step the options name and suggest email.
- **Send time:** now or a local time; times are in the store's time zone.
- **The offer and the one action** you want people to take.

Look at past results before you write: `chargezen.smartytap_campaigns.list.v1` with `status: "completed"`, then `chargezen.smartytap_campaigns.report.v1` on the two or three most recent, to reuse what got clicks.

## 2. Draft it

1. `chargezen.smartytap_campaigns.create.v2` with a new `operation_id`. Start the email from a fitting template or starter design named in the options.
2. Write the email at the document address the result gives, with `chargezen.email_documents.apply_ops.v1`: a subject under 50 characters, preview text that adds to it, one clear headline, short body, one button, the unsubscribe link and mailing address. Use personalization tokens exactly as the options list them.
3. Texts: under 160 characters where you can (each part costs credits), the store name first, one link, and the opt-out wording the workspace uses.
4. Offer an A/B test when the list is large enough to learn from (`/campaign-ab-test`): an email's versions are added with `chargezen.smartytap_campaigns.add_versions.v1`; a text's are written inline in its `versions` (Version A is `body`), and each version is a paid text, so it costs more.
5. If they group campaigns (such as Black Friday), set the campaign's `tags`.

## 3. Check it

- `chargezen.smartytap_campaigns.review.v1`: fix everything it lists before going on.
- `chargezen.smartytap_campaigns.preview.v2` to read the email as customers will.
- `chargezen.smartytap_campaigns.preview_audience.v1`: how many people can receive each message, and for texts the estimated credit cost against the balance.

Show the person: subject and preview text, a short summary of the body, who gets it (with the count), when it sends, and what texts cost.

## 4. Test, then launch

- On their OK, `chargezen.smartytap_campaigns.send_test.v2` to them (new `operation_id`).
- Launch only when they say to: `chargezen.smartytap_campaigns.launch.v1` confirms the recipients, text cost and revision you just showed; if any of those changed, show the new figures and ask again.
- An email whose coupon block gives each person their own code makes one real single-use Shopify discount code per recipient as it sends (`discount_codes` in `chargezen.smartytap_campaigns.preview_audience.v1`); say so with that number before launch. Emails only; a text can't carry one.
- If `chargezen.smartytap_campaigns.get.v1` later shows `discount_codes`, sending is paused over those codes; relay its `message` and act on its `state`:
  - `unfinished` (Shopify didn't finish the codes): on their OK, resume with `chargezen.smartytap_campaigns.resume.v1`; Shopify is asked again and the waiting emails send once their codes work.
  - `refused` (Shopify refused the discount, or the store is disconnected): give Shopify's reason from `message`, change the coupon block's offer with `chargezen.email_documents.apply_ops.v1`, and on their OK publish it with `chargezen.smartytap_campaigns.publish_scheduled_edit.v1`. Resuming alone pauses again.
  - An offer changed after launch gives every unsent email a new code for the new offer; old unused codes stay in Shopify until they expire.
- After it sends, offer to read the results with `chargezen.smartytap_campaigns.report.v1` the next day (`/campaign-results`).
