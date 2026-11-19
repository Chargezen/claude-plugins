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

Build, test, schedule, launch, manage and report on email, text and WhatsApp campaigns; A/B tests and translations; welcome, abandoned cart, back-in-stock, thank-you, order-tag and birthday flows, and a health check on them all; marketing reports, each flow's step results and your store's recorded events; people, consent, imports (including from Klaviyo), timelines, custom properties, exports, lists and segments, merging duplicates and cleaning them up; sign-up forms and how they convert; surveys and their results; brand email templates, shared sections and images; WhatsApp templates; texting setup, carrier registration, numbers and countries; email domains, mailboxes and senders; one-to-one texts and emails; replying from the inbox.

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
| `/flow-health` | Read-only check of every flow: what's on or off, broken emails and texts, unapproved WhatsApp templates, runs that stopped and why, overlaps and missing journeys, with a ranked list of fixes |
| `/segment <who>` | Builds, reads or changes a live audience (VIPs, lapsed buyers, unengaged, product buyers, survey answers), changing only the rule you ask for, counted with sample names before it's saved; lists who is in it now, shows how it grew and tags it |
| `/list-import <people>` | Imports subscribers with their consent and custom properties, reports who was added or skipped and why, handles single opt-ins and opt-outs (texts, WhatsApp and email), shows how a list grew and one person's timeline, sets custom properties and exports contacts to a file, counted first |
| `/klaviyo-import [list] [SmartyTap list]` | Brings a Klaviyo list or segment into a SmartyTap list straight from your connected Klaviyo account, with each person's consent as Klaviyo recorded it and every Klaviyo unsubscribe applied, sending nothing, then reports what was recorded and skipped |
| `/sender-setup` | Gets texting and email ready: texting set up from nothing (business details, a first toll-free number and its carrier verification, local-texting registration), numbers and countries, and your own email domain, footer, team sender and default sender, each bought or submitted only on your OK |
| `/whatsapp-template <message>` | Writes a WhatsApp marketing template, submits it to Meta on your OK, checks the answer and fixes a rejection |
| `/email-template` | Makes a reusable on-brand email template from a campaign that worked, a copy or a starter design; sends you a test of a template, renames or retires templates, keeps a shared footer in every campaign email and updates it in every email that uses it at once, and adds images from your site |
| `/translate-campaign <campaign> <language>` | Adds a version of a campaign message for customers whose profile language matches, written in that language and counted before launch |
| `/campaign-ab-test <campaign>` | Sets up a subject-line, content or send-time test on a campaign email, or two versions of a text, reads how each version is doing and picks the winner on your OK |
| `/campaign-results [days]` | Read-only review of recent campaigns: delivered, opened, clicked, unsubscribed, orders and revenue, channels compared, then three takeaways |
| `/marketing-report [days]` | Read-only: how email, text and WhatsApp did against the period before, the campaigns and flows behind it, and subscriber growth, text deliverability and plan usage on request |
| `/flow-results [days] [flow]` | Read-only: every flow's results for the period, then each step of the ones that matter for the same days to find the weakest email or text |
| `/event-metrics <question> [days]` | Read-only: one event your storefront recorded (placed orders, add-to-carts, product views) counted, counted by person or added up by day, split by currency or state, or for a segment's people |
| `/audience-cleanup` | Lists segments and lists with their sizes, deletes the ones you confirm by name (the people always stay), frees one a scheduled campaign still uses, takes people off a list, merges two profiles of the same person and deletes a contact you confirm |
| `/signup-form <form>` | Builds a popup, flyout, embedded or back-in-stock sign-up form with its list and offer as a draft, publishes it on your OK, reports how forms convert (all time) and turns one off |
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
- `/marketing-report 30`
- `/signup-form 10% off email popup`
- "Which email in my welcome flow is weakest?"
