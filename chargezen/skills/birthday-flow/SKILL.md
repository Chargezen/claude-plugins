---
name: birthday-flow
description: Build a yearly SmartyTap flow in Chargezen on a date saved on each person's profile — a birthday message, or an anniversary of the day they joined — sent on the day or a set number of days before or after, saved as a draft and turned on only on the merchant's OK. Also sets up collecting birthdays with a survey when the store doesn't have them yet. Use for birthday or anniversary emails and texts.
argument-hint: "[birthday | joined anniversary] [offer]"
---

# Birthday and anniversary flow

The request: $ARGUMENTS

Follow the `chargezen` skill for how to reach the tools.

## 1. Find the date

The trigger is **Date on the profile** (`smartytap.profile.date_property`). It runs every year on a date in each person's profile, with an offset of up to 365 days before or after (0 is on the day). The date is either:

- the day they joined (`field` `created_at`), for a "one year with us" anniversary; or
- a custom date property, such as `birthday`.

Check the property exists and is filled: `chargezen.smartytap_segments.fields.v1` lists the workspace's custom properties, and `chargezen.smartytap_segments.preview.v1` with a condition on that property (using an operator the fields list for it) counts how many people have it. If few or none do, nothing will send. Offer to collect it first:

- a survey with a `date` question whose `property` is `birthday` (`/survey`), linked from an email or a campaign. Answers save to the profile.

## 2. Agree the plan

1. **Trigger:** Date on the profile, the property, and the offset (for example −7 to give a week to use a birthday code).
2. **Email**, and a **text** if texts are ready: a warm note, one clear gift. A gift must be a real discount code from their store, named exactly; this connection can't check codes, so ask. Never invent one.
3. Optional **Wait** and a reminder near the end of the gift's window, with a profile filter history `placed_order` equals 0 `since_flow_start` so buyers aren't reminded.
4. **Re-entry:** `allow`, so it runs every year.

These are marketing messages: only people who agreed to email or texts get them.

## 3. Build, check, turn on

1. `chargezen.workflows.authoring_options.v1` for senders, starter designs and personalization; `chargezen.workflows.list.v1` to avoid a second birthday flow.
2. `chargezen.workflows.create.v2` with `status: "draft"`, the `date_property` setting and a new `operation_id`.
3. Write the email with `chargezen.email_documents.apply_ops.v1`; check with `chargezen.workflows.preview_email.v2` and `chargezen.workflows.preview_sms.v1` (trigger `smartytap.profile.date_property`).
4. Show the messages, when they send relative to the date, and how many people have the date today. Only when they say so: `chargezen.workflows.activate.v1`.
