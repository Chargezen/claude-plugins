# Chargezen SmartyTap for Claude

Run SmartyTap email, text and WhatsApp marketing from Claude with Chargezen: campaigns, automatic flows, lists, segments, surveys and the inbox.

## Requirements

- A Chargezen workspace with SmartyTap (new? you can create an account when you connect)
- A Chargezen teammate role that can use SmartyTap

## Install

```
/plugin marketplace add chargezen/claude-plugins
/plugin install chargezen-smartytap@chargezen
```

Then run `/mcp`, choose `chargezen-smartytap` and sign in. You'll sign in to Chargezen, pick your workspaces and approve what Claude may do. To disconnect, remove it in Claude, or in Chargezen open **Settings → Connected AI assistants**. Full guide: https://chargezen.com/mcp

Want every Chargezen product in one connection, plus the weekly brief, win-back and failed-payment skills? Install `chargezen@chargezen` instead.

## What Claude can do

Build, test, schedule, launch, manage and report on email, text and WhatsApp campaigns; A/B tests and translations; welcome, abandoned cart, back-in-stock, thank-you, order-tag and birthday flows, and a health check on them all; people, consent, imports, lists and segments; surveys and their results; brand email templates; WhatsApp templates, texting numbers and senders; one-to-one texts and emails; replying from the inbox.

## What's included

| Part | What it does |
|---|---|
| `chargezen-smartytap` MCP server | Connects to `https://mcp.chargezen.com/mcp/smartytap`, only SmartyTap's tools, so Claude has fewer to choose from |
| `chargezen` skill | Teaches Claude how to reach the tools, the safe order for changes (read → draft → preview → go live) and the rules it never breaks |
| `/campaign <brief>` | Builds an email, text or WhatsApp campaign as a draft from a short brief, fixes what Review flags, counts who gets it and what texts cost, sends you a test, and launches when you say so |
| `/inbox-triage [count]` | Works through customers waiting on a reply, oldest first, drafts a reply for you to approve, then sends, assigns, tags or closes |
| `/welcome-series [list]` | Builds a welcome flow for new email and text subscribers: a first message right away, a follow-up a few days later, leaving out people you imported |
| `/abandoned-cart [checkout, cart or browse]` | Builds abandoned checkout, abandoned cart or browse abandonment flows: an email, then a text, with their items and a link back, stopping when they order |
| `/back-in-stock` | Builds a flow that emails and texts each shopper who asked about a product the moment it's back |
| `/order-follow-up` | A thank-you after an order ships, then a review request or a quick rating by text, with a different path for first-time customers if you like |
| `/order-tag-flow <tag> <action>` | Runs when an order gets a tag in Shopify: message the customer, alert your team, hold the order from shipping or tag it again |
| `/birthday-flow` | A yearly birthday or join-date anniversary message, on the day or days before, and a survey to collect birthdays if you don't have them |
| `/flow-health` | Read-only check of every flow: what's on or off, broken emails and texts, unapproved WhatsApp templates, overlaps and missing journeys, with a ranked list of fixes |
| `/segment <who>` | Builds or changes a live audience (VIPs, lapsed buyers, unengaged, product buyers, survey answers), counted with sample names before it's saved |
| `/list-import <people>` | Imports subscribers with their consent recorded, reports who was added or skipped and why, and handles single opt-ins and opt-outs |
| `/sender-setup` | Gets texting ready: what setup still needs, the countries you text, another local or toll-free number you pick and approve, and a team email sender |
| `/whatsapp-template <message>` | Writes a WhatsApp marketing template, submits it to Meta on your OK, checks the answer and fixes a rejection |
| `/email-template` | Makes a reusable on-brand email template from a campaign that worked, a copy of a template or a starter design |
| `/translate-campaign <campaign> <language>` | Adds a version of a campaign message for customers whose profile language matches, written in that language and counted before launch |
| `/campaign-ab-test <campaign>` | Sets up a subject-line, content or send-time test on a campaign email, reads how each version is doing and picks the winner on your OK |
| `/campaign-results [days]` | Read-only review of recent campaigns: delivered, opened, clicked, unsubscribed, orders and revenue, channels compared, then three takeaways |
| `/marketing-calendar [month]` | Plans a month of campaigns from past results and your launches and sales, then drafts each one on the campaign calendar for you to launch |
| `/survey <question>` | Builds a survey (how did you hear about us, NPS, feedback, birthdays) with an optional free gift, puts it live on your OK, sends it and reads the results |
| `/direct-message <who> <what>` | Writes one person a text or email from your number or mailbox, saving them as a contact if they're new, now or scheduled for later |
| `/manage-campaign <campaign> <change>` | Pauses, resumes, reschedules, fixes, stops, archives or deletes a scheduled or sending campaign, showing what will still go out |

Claude asks before anything reaches your customers or changes your store. The skills are copied from [`chargezen/skills`](../chargezen/skills); edit them there and run `scripts/sync-product-plugins.py`.

## Try

- `/campaign Holiday bundle to the VIP list, Friday 9am`
- "How many people will get this text, and what will it cost?"
- `/abandoned-cart checkout`
- `/survey how did you hear about us, for new customers`
- `/marketing-calendar December, holiday sale on the 12th`
- "Push tomorrow's newsletter to Friday 9am."
- "Build a browse abandonment flow and turn it on."
