---
name: email-template
description: Look after SmartyTap's email template library in Chargezen — list and read templates, make a reusable on-brand template from a campaign email that worked, a copy or a starter design, rename or retire old ones, save a footer or header as a reusable section used in every campaign email, send a test of a template to an inbox, and add images from the store's website. Use when they want a brand template, a newsletter layout, to save an email as a template, to tidy the template library, a shared footer, "send me a preview of this template", or to put an image from their site in an email.
argument-hint: "[what to do] [template name]"
---

# Email templates, sections and images

The request: $ARGUMENTS

Follow the `chargezen` skill for how to reach the tools.

## 1. See what's there

- `chargezen.smartytap_email_templates.list.v1`: the active templates and saved sections and blocks, most recently changed first (narrow with `query`), each with its document address and, for a saved section, how many campaign emails hold a linked copy. Retired templates aren't listed; read one by its `template_id` with `chargezen.smartytap_email_templates.get.v1`.
- `chargezen.smartytap_campaigns.authoring_options.v1`: the brand (store address, logo, colors, fonts, brand styles) and Chargezen's starter designs (with a `starter_key`, such as Welcome, Product launch, VIP thank-you). If the brand has no colors or logo yet, ask for them or a link to the site.

## 2. Make a template

- **From a campaign email that worked:** find it (`chargezen.smartytap_reports.campaigns.v1` to see what did well, `chargezen.smartytap_campaigns.get.v1` for its email's document address). Save it, or one of its A/B versions, with `chargezen.smartytap_email_templates.create_from_email.v2` (its document address, a name, a new `operation_id`).
- **From an existing template:** copy it with `chargezen.smartytap_email_templates.copy.v2`, then change the copy; the original stays as it was.
- **From a starter design:** the library copies only the workspace's own templates, so build it in a draft campaign: `chargezen.smartytap_campaigns.create.v2` with the email started from the `starter_key`, style it (step 3), save it with `chargezen.smartytap_email_templates.create_from_email.v2`, then offer to delete the scratch draft with `chargezen.smartytap_campaigns.delete.v1` (it has sent nothing).

## 3. Make it on-brand

Read the email with `chargezen.email_documents.get.v1` (the outline lists every section and block by id), then change it with `chargezen.email_documents.apply_ops.v1` from that revision:

- `apply_brand` with a brand style, or `set_settings` for width, colors and fonts;
- the logo at the top, a clear headline block, body text, one button style, a footer with the mailing address and unsubscribe link;
- placeholder words that say what goes there ("Headline: one line about the offer"), so whoever uses it knows what to replace;
- `set_subject` and `set_preheader` with sample text.

Check it with `chargezen.email_documents.preview.v2` and show the person the preview and the template name.

**To see it in an inbox** ("send me a preview of this template"): `chargezen.smartytap_email_templates.send_test.v1` with its `template_id` and a new `operation_id` (keep it for any retry; a new one sends another test). It sends the template as saved now, subject starting with [Test], personalization filled with sample data, to the teammate's own email address. Pass `recipient` only when the teammate names another address (a colleague or a test inbox); never pick one yourself. No campaign or customer is involved and no one's consent or counts change. If it's refused because the workspace has no default sender, say so and offer to set one with `chargezen.email_channel.set_default_sender.v1` (`/sender-setup`). If `sent` is false, say why from `detail`, such as waiting for email send approval. `chargezen.email_documents.undo.v1` takes back the last change if they don't like it. A template's content is edited the same way, at the document address `chargezen.smartytap_email_templates.get.v1` returns.

## 4. Rename or retire

`chargezen.smartytap_email_templates.update.v1` renames a template or saved section, retires it (`status: "archived"`) or brings it back (`status: "active"`). Templates can't be deleted: retiring is how an old one leaves the library. A retired template isn't listed and can't be started from, copied or put in an email any more; emails already made from it keep their content. Confirm the names before retiring several.

## 5. A reusable section (a shared footer or header)

1. Find the campaign email that has the section as it should be, and the section's or block's id in the outline from `chargezen.email_documents.get.v1`.
2. `chargezen.smartytap_email_templates.create_section.v1` with that email's address, the `node_id`, a name ("Footer") and a new `operation_id`. The email it came from keeps its part unchanged and not linked.
3. Put it in each campaign email with the `insert_universal` op in `chargezen.email_documents.apply_ops.v1`, its `universal_id` being the returned `template_id`. Each email gets its own linked copy.
4. **Later changes:** edit the saved section at its document address. Emails already using it don't change until each one is brought up to date with the `refresh_universal` op on that email. `chargezen.smartytap_email_templates.get.v1` on the section lists how many linked copies there are and some of the emails holding them; say which ones you refreshed and which you didn't.

## 6. Images

- `chargezen.smartytap_images.list.v1`: the image library, newest first (narrow with `query`), each with the URL emails load it from.
- **An image from their website:** `chargezen.smartytap_images.add_from_url.v1` with its address, a name and alt text. Chargezen saves the address, not a copy of the image: emails load it from their site, so it shows only while the site serves that address and changes if the site changes it. Tell the merchant this before adding, and suggest an address they control.
- Put an image in an email with `chargezen.email_documents.apply_ops.v1`: an image block's `assetId` set to its `image_id`, and its `imageUrl` and `src` to its URL.
- **Tidy up:** `chargezen.smartytap_images.update.v1` renames it, changes its alt text, or archives it (hidden from the library and image picker, still showing in every email that uses it). Prefer archiving. `chargezen.smartytap_images.delete.v1` removes it for good: an uploaded image's file goes with it, so every email showing it, including ones already sent, shows a broken image. Delete only on a clear yes after saying so.

## 7. Use it

New campaign emails start from a template by `template_id` (`/campaign`), and so can new flow email steps. Changing a template later doesn't change emails already made from it.
