---
name: list-import
description: Put people on a SmartyTap list in Chargezen with their marketing consent recorded properly — a spreadsheet of email or text subscribers, sign-ups from an event, or one person who agreed in person — then follow the import and report who was added and who was skipped and why. Imports custom properties such as birthdays or points with the people. Also adds people to a list without consent, records one person's consent, unsubscribes someone from texts, WhatsApp or email on request, shows how a list grew, shows what one person was sent and did lately, sets their custom properties, and exports contacts to a file. Use for importing subscribers, moving a list from another tool, recording opt-ins and opt-outs, list growth, a contact's timeline or properties, or a contacts export.
argument-hint: "<the people or file> [list name]"
---

# List import and consent

The request: $ARGUMENTS

Follow the `chargezen` skill for how to reach the tools.

## 1. Consent comes first

Ask how these people agreed to get marketing, in the merchant's words. That statement is recorded as evidence.

- **They agreed** (a sign-up form, a checkout checkbox, a booth sign-up sheet, their old email tool's subscribers): import with consent (step 2).
- **They didn't, or the merchant isn't sure** (customers who never opted in, a bought or shared list): don't import with consent. Offer to put them on a list without consent (step 3), which lets the team see and group them but sends them no marketing.

Texts need more: express written consent, how they gave it (`consent_source`) and the date (`consented_on`). Without both, import for email only.

## 2. Import with consent

1. Pick the list: `chargezen.smartytap_lists.list.v1`, or a new name. Read the people from what the merchant gave: email for an email import, phone for a text import, plus first and last name, company or website, and tags for text imports.
   - **Custom properties** (a birthday, a loyalty tier, points): give each person's as `custom_properties`, by a name of letters, numbers and underscores (not `first_name` or `last_name`). Each is saved on their profile, replacing a property of the same name. A property you give as a JSON number **for everyone who has it in this call** is saved as a number, which segment comparisons such as "points greater than 1000" need; if even one person's value is text, it's saved as text for all. So send counts and amounts as numbers, and ids, zip codes and phone-like values as text (a leading zero must survive). Write dates as `YYYY-MM-DD`, or `MM-DD` for a yearly date such as a birthday without a year; a date property can start a "Date on the profile" flow for them on that date, so say so.
2. Show the person: the list, the channel, how many people, the custom properties and their types, five sample rows, rows you dropped (no email or phone, clear typos) and the consent statement as you'll record it.
3. On their OK: `chargezen.smartytap_lists.import.v1` with `consent_confirmed: true`, the consent details and a new `operation_id`. Keep that `operation_id` for any retry.
4. Follow it with `chargezen.smartytap_lists.get_import.v1` until it's `completed` or `failed`. Report how many were added, already on the list, skipped and invalid, with the skipped reasons grouped. Anyone who unsubscribed, texted STOP, bounced or marked mail as spam is never subscribed again; say that's working as intended.

Importing sends nothing. Chargezen's welcome flows leave imported people out; a flow of the workspace's own on "Subscribed to a list" without that filter would welcome them. Check `chargezen.workflows.list.v1` and say so if one would.

## 3. Other jobs

- **On a list, no consent:** `chargezen.smartytap_lists.create.v1` if needed, then `chargezen.smartytap_lists.add_contacts.v1` with their contact ids (`chargezen.contacts.search.v1`; save someone new with `chargezen.contacts.create.v1` first). Lists built from conditions can't take people by hand.
- **One person who agreed:** `chargezen.contacts.search.v1` or `chargezen.contacts.create.v1`, then `chargezen.contacts.record_consent.v1` for `email` or `sms` (texts need how and when).
- **Who's on a list:** `chargezen.smartytap_lists.members.v1`. Consent is shown, not filtered.
- **Unsubscribe someone** when they ask: `chargezen.contacts.opt_out.v1` with the channel and their reason, one call per channel.
  - `sms` or `whatsapp` unsubscribes a phone number. After a text opt-out nobody on the team can text them one to one either, and only they can opt back in (texting START, or sending a WhatsApp message).
  - `email` unsubscribes the contact's main email address (give their `contact_id`), recorded as their own unsubscribe link would. It stops **marketing email only**: campaigns and marketing flow emails skip the address, while one-to-one emails from the inbox, a flow's transactional emails and the store's order and account emails still reach it. Say that in one line.
  - Only the person can subscribe again (texting START, or signing up with a form for email). Never use `chargezen.contacts.record_consent.v1` to resubscribe someone who unsubscribed; it leaves an unsubscribed address as it is.
  - Never delete a contact or take them off a list to stop their marketing: neither unsubscribes anyone.
- **How a list grew:** `chargezen.smartytap_lists.growth.v1` with its `list_id` and `start_date` and `end_date` (at most 366 days apart): how many people were on it each day and the net change between the first and last day with a count. A count is recorded only when the list's count is refreshed (people added, removed or imported by a teammate, a list made or copied; sign-ups from forms and keywords don't refresh it on their own). History starts at `recorded_since`, and a day with a null count is unknown, **never zero and never "no growth"**. It's the list's size, not consent: for subscribers gained and lost by channel, use `chargezen.smartytap_reports.subscriber_growth.v1`.
- **Tags:** `chargezen.smartytap_lists.create.v1` takes `tags`, and `chargezen.smartytap_lists.update.v1` changes them; `chargezen.smartytap_lists.list.v1` with an exact `tag` lists the lists carrying it.
- **Take people off a list** or delete a contact: `/audience-cleanup`.
- **Rename a list:** `chargezen.smartytap_lists.update.v1`. A flow filtered on the old list name stops matching; check `chargezen.workflows.list.v1` and say so.
- **One list's details:** `chargezen.smartytap_lists.get.v1`: how it was made, whether it takes new sign-ups, how many are on it and its subscribe page. To delete lists, use `/audience-cleanup`.

## 4. One person

- **What they were sent and did lately:** `chargezen.contacts.get.v1`: their consent per channel, lists, tags, custom properties, conversations, and the timeline: messages sent to them, what they texted, flows they entered, orders and consent changes, with the message text. That brings their messages and orders into this conversation; share only what the merchant asked about.
- **Set a custom property:** read them first with `chargezen.contacts.get.v1`, then `chargezen.contacts.update.v1` with the property. What was there before is overwritten. Segments, flow conditions, text personalization and "Date on the profile" flows read these properties, so a change can move them into or out of a segment or a flow path, and a date property can start such a flow for them on that date: say so before saving. A language or time zone the customer chose themselves can't be changed, and the whole edit is then refused.

## 5. Export contacts

`chargezen.contacts.export.v1` makes a CSV of everyone, or of the people `chargezen.contacts.search.v1` finds with the same search and filters (name, email or phone, stage, text consent, preferred channel, tag, company), with name, phone, email, text consent, stage and tags.

- It exports the Contacts list, not one list's or segment's members. For who is on a list, use `chargezen.smartytap_lists.members.v1` above.
- Say first that the file takes customers' personal data out of Chargezen, and that anyone in the workspace who can open Contacts can download it. Start it only on their OK.
- Use **one `operation_id` per export** and keep it for any retry; a new one makes another file.
- Follow it with `chargezen.contacts.get_export.v1` until it's ready, then hand the merchant the download link (the same one they're emailed); it opens Contacts and downloads after they sign in. **Never paste rows** into the conversation; the tools don't return them. An export that keeps reading `in_progress` can be started again with a new `operation_id`.
