---
name: get-started
description: Set up and tour Chargezen right after the plugin is installed — what Chargezen is, how to connect a workspace, how its tools are found and run, and three useful things to try first. Use when the person has just installed the plugin, asks what Chargezen can do, or asks how to get started.
---

# Get started with Chargezen

Explicit instructions from the person always come before this guide. Follow the `chargezen` skill for every call you make.

## 1. Say what Chargezen is

In two or three short sentences: Chargezen runs a brand's customer conversations, subscriptions, email and text marketing, checkout offers, loyalty and creator programs in one place. Its products are Concierge (AI agents that answer customers), Subscriptions, CheckoutOS (checkout offers and upsells), SmartyTap (email, text and WhatsApp marketing and the inbox) and Spark! (affiliates and creators). Through this plugin you work in their Chargezen workspace as them, with the permissions they already have.

## 2. Connect

1. Call `chargezen.connection.get_profile.v1`. If it answers, the connection works: say who they are connected as and name the workspaces it reaches. When there is more than one, ask which brand to start with and pass that `workspace` on every later call.
2. If the call asks them to sign in or the connection is missing, tell them to connect Chargezen when ChatGPT prompts them, sign in, pick the workspaces to share and press Allow. Someone new to Chargezen can create an account on that sign-in screen. Never ask for their password or a sign-in code in the chat.
3. Mention once that owners and admins get an email when an assistant is connected, and that anyone can disconnect it in Chargezen under **Settings → Connected AI assistants**.

## 3. How the tools are found

Explain this briefly only if they ask; otherwise just use it.

- Every tool this connection can use is listed and called directly by its name. `chargezen.tools.index.v1` searches them (narrow it with `namespaces` or `query`).
- Chargezen checks their permissions and plan on every call. Changes that customers would see (launching, publishing, sending, cancelling, deleting) wait for their explicit OK.

## 4. Offer three things to try

Offer these three, in plain words, and run the one they pick:

1. **See what's waiting in the inbox:** the open customer conversations, who has each one, and drafts of replies for them to approve (`inbox-triage` skill).
2. **Get a weekly brief:** sales, new and canceled subscriptions, campaign and offer results for the last 7 days (`weekly-brief` skill).
3. **Draft a campaign without sending it:** an email or text campaign from a one-line brief, saved as a draft with the audience count, for them to review (`campaign` skill).

End with one line: they can ask for anything in their workspace in their own words, such as "skip Sam's next order" or "how did last week's email do?".
