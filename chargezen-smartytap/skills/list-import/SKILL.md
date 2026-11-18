---
name: list-import
description: Put people on a SmartyTap list in Chargezen with their marketing consent recorded properly — a spreadsheet of email or text subscribers, sign-ups from an event, or one person who agreed in person — then follow the import and report who was added and who was skipped and why. Also adds people to a list without consent, records one person's consent, and unsubscribes a number on request. Use for importing subscribers, moving a list from another tool, or recording opt-ins and opt-outs.
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

1. Pick the list: `smartytap_lists.list`, or a new name. Read the people from what the merchant gave: email for an email import, phone for a text import, plus first and last name, company or website, and tags for text imports.
2. Show the person: the list, the channel, how many people, five sample rows, rows you dropped (no email or phone, clear typos) and the consent statement as you'll record it.
3. On their OK: `smartytap_lists.import` with `consent_confirmed: true`, the consent details and a new `operation_id`. Keep that `operation_id` for any retry.
4. Follow it with `smartytap_lists.get_import` until it's `completed` or `failed`. Report how many were added, already on the list, skipped and invalid, with the skipped reasons grouped. Anyone who unsubscribed, texted STOP, bounced or marked mail as spam is never subscribed again; say that's working as intended.

Importing sends nothing. Chargezen's welcome flows leave imported people out; a flow of the workspace's own on "Subscribed to a list" without that filter would welcome them. Check `workflows.list` and say so if one would.

## 3. Other jobs

- **On a list, no consent:** `smartytap_lists.create` if needed, then `smartytap_lists.add_contacts` with their contact ids (`contacts.search`; save someone new with `contacts.create` first). Lists built from conditions can't take people by hand.
- **One person who agreed:** `contacts.search` or `contacts.create`, then `contacts.record_consent` for `email` or `sms` (texts need how and when).
- **Who's on a list:** `smartytap_lists.members`. Consent is shown, not filtered.
- **Unsubscribe a number** when someone asks: `contacts.opt_out` for `sms` or `whatsapp` with their reason; for both, two calls. After a text opt-out nobody on the team can text them one to one either, and only they can opt back in (texting START). Email unsubscribes aren't done with these tools: the person uses the unsubscribe link every marketing email carries.
- **Rename a list:** `smartytap_lists.update`. A flow filtered on the old list name stops matching; check `workflows.list` and say so.
