---
name: chat-launcher
description: Design and publish the storefront chat launcher in Chargezen Concierge — the chat button, its teaser message, the greeting, shortcut cards, FAQ cards, away message, the store's colors, fonts and logo, and where it sits on the page — saved as a draft, described in plain words with a link to preview it, and published only on the merchant's OK, then switched on in the Shopify theme by the merchant. Use when they want chat on their store, want the launcher to match their brand, or want to change its greeting, teaser, FAQs or position.
argument-hint: "[what to change]"
---

# Chat launcher

The request: $ARGUMENTS

Follow the `chargezen` skill for how to reach the tools. **Read only** until the person approves a draft.

## 1. See what's there

1. `web_chat.get`: the editable draft, the published launcher shoppers see now (or that none is published), the assistant name (Concierge or Finn), the web chat channel and the agent answering it, the installation details and `editor_url`, where the merchant can preview it.
2. `workspace_brand.get`: the store's name, logo, colors and fonts, to match the launcher to them.
3. `channels.list`: whether storefront chat is ready and who answers it.

Tell them in two lines what shoppers see today and what the draft holds if it differs.

## 2. Agree the changes

Ask only what isn't clear, and propose a launcher in the store's voice:

- **Button and teaser:** the teaser message next to the button (short, such as "Questions? We're here"), when it appears (after a few seconds, halfway down the page, when leaving, or never) and whether it shows on every page.
- **Home view:** the brand header (logo from the brand settings), a two-line greeting (a small line, then the headline), shortcut cards (orders, subscriptions, rewards and so on), the message box prompt, and up to a handful of FAQ cards. Write FAQ answers only from facts the store has (`knowledge.search`); leave a clear blank for anything unknown.
- **Look:** a color scheme or the brand's own colors, fonts, corner rounding.
- **Position and behavior:** left or right, offsets, hide on phones, open on the first page, message sound, and an away message for when nobody answers.
- **Assistant name:** Concierge or Finn. Changing it shows the new name to shoppers at once, even before publishing: say so.

Start from the draft `web_chat.get` returned and change only what was agreed; keep every other section, block and setting as it is, and keep the order of sections the way shoppers should see them.

## 3. Save the draft

`web_chat.save` with the complete draft (anything left out is removed). Shoppers keep seeing the published launcher. Describe the new launcher in a few plain lines and give `editor_url` so they can preview it. If it's refused, explain why in plain words, fix it and save again.

## 4. Publish only when they say so

Ask: "Publish this launcher? It replaces what shoppers see on your store now." On an explicit yes, `web_chat.publish`. Publishing also turns on the web chat channel.

## 5. What stays with the merchant

- **Show it on the store:** in the Shopify theme editor, under App embeds, turn on **Concierge Widget** and save. These tools can't do that step; until it's on, shoppers don't see the launcher.
- **Someone to answer:** if no active agent answers web chat, offer `/support-agent` to set one up, or `/channel-setup` to give it to an existing agent.

End with what's live, what's still a draft, and the next step.
