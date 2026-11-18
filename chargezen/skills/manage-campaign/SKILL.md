---
name: manage-campaign
description: Change a SmartyTap campaign in Chargezen that's already scheduled or sending — pause and resume it, move it to another time or audience, fix a typo in an email that hasn't reached everyone, stop one message or the whole campaign, archive a sent one, or delete one that never sent — showing exactly what will and won't still go out, and acting only on the merchant's OK. Use when they say "stop that campaign", "push it to tomorrow", "fix the subject", or ask what's scheduled.
argument-hint: "<campaign> <what to change>"
---

# Manage a campaign

The request: $ARGUMENTS

Follow the `chargezen` skill for how to reach the tools.

## 1. Find it and its state

`smartytap_campaigns.list` (by name, or status `scheduled`, `active` or `paused`), then `smartytap_campaigns.get`: each message's send status (`scheduled`, `preparing`, `sending`, `ab_test_running`, `sent`…) and recipient counts. Tell the person in one line what has gone out and what's still waiting. What's already sent can't be taken back.

## 2. Pick the right action

| They want | Do this | What happens |
|---|---|---|
| Hold it for now | `pause` | Unsent messages wait, nothing is lost; times that pass while paused send once resumed |
| Carry on | `resume` | Waiting messages send, including any whose time passed |
| Another time or audience, a text changed, before anything has sent | `unschedule`, then `update`, then `preview_audience` and `launch` again | Back to a draft with its send times kept; recipients are counted again at relaunch |
| Fix an email that's scheduled or sending | `email_documents.apply_ops` on the email, then `publish_scheduled_edit` | People who haven't got it yet get the fixed version; anyone already sent keeps the old one |
| Stop one message | `cancel` with its channel (and message id) | That message's unsent sends are cancelled; the rest keeps going |
| Stop everything, for good | `cancel` | Nothing more sends; it can't be edited or relaunched (copy it with `duplicate` to start again) |
| Tidy up a sent campaign | `archive` | Unsent messages are cancelled for good; results stay available |
| Remove one that never sent | `delete` | Gone for good, with its content; refused once anything has sent |

Notes:
- `unschedule` is refused once any message has started sending: then the choices are pausing, fixing a waiting email, or cancelling what's left.
- `publish_scheduled_edit` is for emails. A text in a campaign that's sending can't be edited; cancel that message and send a corrected one in a new campaign if it matters.
- After `publish_scheduled_edit`, 0 updated sends means none had been prepared yet (they're prepared at the send time), not that the fix was lost.
- A campaign the plan's contact limit paused resumes with `resume`, but pauses again if the workspace is still over the limit.

## 3. Confirm, act, report

Say in one sentence what you'll do and what customers will and won't get (such as "Pause the Black Friday campaign: the texts not yet sent will wait until you resume", with the real counts from `get`). Act only on their yes. Relaunching follows the `/campaign` launch steps: show the new recipient count and text cost and confirm again. Report the campaign's state afterwards.
