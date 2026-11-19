---
name: klaviyo-import
description: Bring a Klaviyo list or segment over into a SmartyTap list in Chargezen, straight from the workspace's connected Klaviyo account, with each person's email and text consent as Klaviyo recorded it and every Klaviyo unsubscribe applied, then follow the import and report what was recorded and skipped. Use for "bring my Klaviyo list over", moving subscribers from Klaviyo to SmartyTap, or importing a Klaviyo segment.
argument-hint: "[Klaviyo list or segment] [SmartyTap list name]"
---

# Klaviyo import

The request: $ARGUMENTS

Follow the `chargezen` skill for how to reach the tools.

**Never move people by reading them through a Klaviyo connector and passing them to `chargezen.smartytap_lists.import.v1`**, even when a Klaviyo connection is right there. That would carry every customer's personal data through this conversation, and it would lose what matters most: each person's consent as Klaviyo recorded it, and the unsubscribes and suppressions in the rest of the Klaviyo account. Chargezen's own Klaviyo import reads Klaviyo directly. If the merchant asks for the other way, say this in one line and use the steps below.

## 1. Pick the source

`chargezen.smartytap_lists.list_klaviyo_sources.v1`: every list and segment in the Klaviyo account saved in Integrations › Klaviyo, by name. It reads names only, no people, and changes nothing.

- `connected` is false: the workspace has no Klaviyo key. Ask them to connect Klaviyo in Chargezen under Integrations › Klaviyo with a private API key, then try again.
- An error says Klaviyo refused the key or the key lacks a scope: relay what it says to enable (read access to lists, segments and profiles) and stop until they've changed the key.

Ask which list or segment to bring over, and which SmartyTap list it goes into: an existing one (`chargezen.smartytap_lists.list.v1` for its `list_id`) or a new one by name.

## 2. Say what will happen, then confirm

Before starting, tell the merchant plainly:

- Each person with an email address or a number that can get texts joins the list with their name; an empty language, time zone, city, country and zip on their profile are filled from Klaviyo, and Klaviyo's custom properties are saved on their profile, replacing a property of the same name.
- **Each person keeps the consent Klaviyo recorded**: someone subscribed to email or texts in Klaviyo is subscribed here with Klaviyo's date and sign-up method as evidence (texts only when Klaviyo has the date); someone who never subscribed joins the list without consent. Nobody who unsubscribed, bounced or complained here is subscribed again.
- **Every unsubscribe and suppression in the whole Klaviyo account is applied here too**, for people not on this list as well, so those addresses and numbers get no marketing email or texts from this workspace. A text opt-out is also written to the store, as any SmartyTap opt-out is (marked on their Shopify customer and sent to the workspace's opt-out webhook).
- A Klaviyo **segment comes over as a snapshot** of who is in it now, into a list; its conditions don't come over and the list won't keep up with it. To keep a live audience, rebuild the conditions with `/segment`.
- **Nothing is sent**, and nothing is written to Klaviyo. Chargezen's welcome flows leave imported people out; a flow of the workspace's own on subscribing without that filter would welcome them, so check `chargezen.workflows.list.v1` and say so if one would.
- It runs in the background, and **a large Klaviyo account takes hours**: Klaviyo limits how fast profiles can be read, and every profile in the account is read for unsubscribes.

Start only on their yes.

## 3. Start it

`chargezen.smartytap_lists.import_from_klaviyo.v1` with `klaviyo_type` and `klaviyo_id` exactly as step 1 returned them, `list_id` or `new_list_name`, and a **new `operation_id`**. Keep that `operation_id` for any retry; it returns the import the first call started. A new one starts another import.

Only one Klaviyo import runs per workspace at a time. If it's refused because another is still running, say so and offer to check on that one instead. Running the same import again later is safe: it adds new people, updates existing ones and records no consent or unsubscribe twice.

## 4. Follow it and report

Read `chargezen.smartytap_lists.get_import.v1` with the returned `import_id` until it's `completed` or `failed`. While it runs, `klaviyo_phase` says whether it's still bringing in the list's people (`members`) or checking the whole account for unsubscribes (`opt_outs`); give the progress in one line rather than reading it again and again in a row.

When it's done, report in plain words:

- how many were added, already there and updated, skipped and invalid, with the skipped reasons grouped (`skipped_rows`);
- the consent recorded, from `consent_counts`: subscribed to email and to texts, Klaviyo unsubscribes and suppressions applied, people kept unsubscribed because they had opted out here, and people subscribed to texts in Klaviyo with no consent date there, imported without text consent; then the account-wide figures (profiles checked, email unsubscribes and suppressions, text unsubscribes applied). A count missing is zero;
- any Klaviyo property names left out (`skipped_property_names`) because they have characters other than letters, numbers and underscores.

If it `failed`, give `error_message` as it reads and what to do next.

End with one offer: see who's on the list (`chargezen.smartytap_lists.members.v1`), or send them a campaign (`/campaign`).
