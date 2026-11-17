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

Build, test, schedule, launch and report on email, text and WhatsApp campaigns; build and edit flows; manage people, consent, lists and segments; surveys, WhatsApp templates, texting numbers and senders; reply from the inbox.

## What's included

| Part | What it does |
|---|---|
| `chargezen-smartytap` MCP server | Connects to `https://mcp.chargezen.com/mcp/smartytap`, only SmartyTap's tools, so Claude has fewer to choose from |
| `chargezen` skill | Teaches Claude how to reach the tools, the safe order for changes (read → draft → preview → go live) and the rules it never breaks |
| `/campaign <brief>` | Builds an email, text or WhatsApp campaign as a draft from a short brief, fixes what Review flags, counts who gets it and what texts cost, sends you a test, and launches when you say so |
| `/inbox-triage [count]` | Works through customers waiting on a reply, oldest first, drafts a reply for you to approve, then sends, assigns, tags or closes |

Claude asks before anything reaches your customers or changes your store. The skills are copied from [`chargezen/skills`](../chargezen/skills); edit them there and run `scripts/sync-product-plugins.py`.

## Try

- `/campaign Holiday bundle to the VIP list, Friday 9am`
- "How many people will get this text, and what will it cost?"
- "Build a browse abandonment flow and turn it on."
