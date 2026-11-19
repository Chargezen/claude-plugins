---
name: manage-campaign
description: Change a SmartyTap campaign in Chargezen that's already scheduled or sending — pause and resume it, move it to another time or audience, fix a typo in an email that hasn't reached everyone, stop one message or the whole campaign, archive a sent one, or delete one that never sent — showing exactly what will and won't still go out, and acting only on the merchant's OK. Use when they say "stop that campaign", "push it to tomorrow", "fix the subject", or ask what's scheduled.
argument-hint: "<campaign> <what to change>"
---

# Manage a campaign

The request: $ARGUMENTS

Follow the `chargezen` skill for how to reach the tools.

## 1. Find it and its state

`chargezen.smartytap_campaigns.list.v1` (by name, by status `scheduled`, `active` or `paused`, or for "everything tagged Black Friday" by the exact `tag`, not `query`; each campaign comes with its tags), then `chargezen.smartytap_campaigns.get.v1`: each message's send status (`scheduled`, `preparing`, `sending`, `ab_test_running`, `sent`…) and recipient counts. Tell the person in one line what has gone out and what's still waiting. What's already sent can't be taken back.

## 2. Pick the right action

| They want | Do this | What happens |
|---|---|---|
| Hold it for now | `chargezen.smartytap_campaigns.pause.v1` | Unsent messages wait, nothing is lost; times that pass while paused send once resumed |
| Carry on | `chargezen.smartytap_campaigns.resume.v1` | Waiting messages send, including any whose time passed |
| Another time or audience, a text changed, before anything has sent | `chargezen.smartytap_campaigns.unschedule.v1`, then `chargezen.smartytap_campaigns.update.v2`, then `chargezen.smartytap_campaigns.preview_audience.v1` and `chargezen.smartytap_campaigns.launch.v1` again | Back to a draft with its send times kept; recipients are counted again at relaunch |
| Fix an email that's scheduled or sending | `chargezen.email_documents.apply_ops.v1` on the email, then `chargezen.smartytap_campaigns.publish_scheduled_edit.v1` | People who haven't got it yet get the fixed version; anyone already sent keeps the old one |
| Stop one message | `chargezen.smartytap_campaigns.cancel.v1` with its channel (and message id) | That message's unsent sends are cancelled; the rest keeps going |
| Stop everything, for good | `chargezen.smartytap_campaigns.cancel.v1` | Nothing more sends; it can't be edited or relaunched (copy it with `chargezen.smartytap_campaigns.duplicate.v2` to start again) |
| Tidy up a sent campaign | `chargezen.smartytap_campaigns.archive.v1` | Unsent messages are cancelled for good; results stay available |
| Remove one that never sent | `chargezen.smartytap_campaigns.delete.v1` | Gone for good, with its content; refused once anything has sent |

Notes:
- `chargezen.smartytap_campaigns.unschedule.v1` is refused once any message has started sending: then the choices are pausing, fixing a waiting email, or cancelling what's left.
- `chargezen.smartytap_campaigns.publish_scheduled_edit.v1` is for emails. A text in a campaign that's sending can't be edited; cancel that message and send a corrected one in a new campaign if it matters.
- After `chargezen.smartytap_campaigns.publish_scheduled_edit.v1`, 0 updated sends means none had been prepared yet (they're prepared at the send time), not that the fix was lost.
- A campaign the plan's contact limit paused resumes with `chargezen.smartytap_campaigns.resume.v1`, but pauses again if the workspace is still over the limit.

## 3. Confirm, act, report

Say in one sentence what you'll do and what customers will and won't get (such as "Pause the Black Friday campaign: the texts not yet sent will wait until you resume", with the real counts from `chargezen.smartytap_campaigns.get.v1`). Act only on their yes. Relaunching follows the `/campaign` launch steps: show the new recipient count and text cost and confirm again. Report the campaign's state afterwards.
