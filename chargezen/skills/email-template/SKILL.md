---
name: email-template
description: Make a reusable on-brand email template in SmartyTap's template library in Chargezen — from a campaign email that worked, a copy of an existing template, or a starter design styled with the store's brand colors, fonts and logo — so future campaigns and flow emails start from it. Use when they want a brand template, a newsletter layout, or to save an email as a template.
argument-hint: "[source email or template] [template name]"
---

# Email template

The request: $ARGUMENTS

Follow the `chargezen` skill for how to reach the tools.

## 1. See the brand and what exists

`smartytap_campaigns.authoring_options`: the brand (store address, logo, colors, fonts, brand styles, image library) and the templates: the workspace's own (with a `template_id`) and Chargezen starter designs (with a `starter_key`, such as Welcome, Product launch, VIP thank-you). If the brand has no colors or logo yet, ask for them or a link to the site.

## 2. Pick the starting point

- **A campaign email that worked:** find it (`smartytap_campaigns.list`, `get`; `report` to confirm it did well). Save it, or one of its A/B versions, with `smartytap_email_templates.create_from_email` (its document address, a name, a new `operation_id`).
- **An existing template:** copy it with `smartytap_email_templates.copy`, then change the copy; the original stays as it was.
- **A starter design:** the library can only copy the workspace's own templates, so build it in a draft campaign: `smartytap_campaigns.create` with the email started from the `starter_key`, style it (step 3), save it with `create_from_email`, then offer to delete the scratch draft with `smartytap_campaigns.delete` (it has sent nothing).

## 3. Make it on-brand

Read the email with `email_documents.get` (the outline lists every section and block by id), then change it with `email_documents.apply_ops` from that revision:

- `apply_brand` with a brand style, or `set_settings` for width, colors and fonts;
- the logo at the top, a clear headline block, body text, one button style, a footer with the mailing address and unsubscribe link;
- placeholder words that say what goes there ("Headline: one line about the offer"), so whoever uses it knows what to replace;
- `set_subject` and `set_preheader` with sample text.

Check it with `email_documents.preview`. Show the person the preview and the template name. `email_documents.undo` takes back the last change if they don't like it.

## 4. Use it

New campaign emails start from it by `template_id` (`/campaign`), and so can new flow email steps. Changing the template later doesn't change emails already made from it.
