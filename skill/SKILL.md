---
name: cpt-prospect-lifecycle
description: >-
  Use whenever the user asks for advice on the Capital Property Training (CPT) sales
  cycle — how to follow up with a prospect, how to reach out, how to get someone booked
  in for a call, how to recover a no-show, how to handle objections after a call, or what
  is being missed at any point from opt-in to onboarding. This skill is the canonical CPT
  funnel: it maps every stage, its trigger/timing, the channels used, what is automated,
  and the manual SOP steps. Use it to locate which stage a prospect is in and give the
  exact channels + automation + SOP for that stage, and to flag any step being skipped.
---

# CPT Prospect Lifecycle — Sales-Cycle Skill

**Canonical source (one source of truth):** the live interactive map.
- Live map: https://capital-property-training.github.io/prospect-lifecycle-map/
- Touchpoints / contact-load per journey: https://capital-property-training.github.io/prospect-lifecycle-map/touchpoints.html

> This file is a text snapshot generated from the live map. The map is canonical — if the map changes, regenerate this skill so they don't drift.

## Business context
CPT sells Rent-to-Rent property mentorship. Funnel: paid-ad opt-in → 8-min VSL → low-ticket Skool course → sales call → high-ticket mentorship. Tools: GoHighLevel (CRM/booking/automation), Skool (course + community), Zapier (GHL→Skool access), WhatsApp, SMS, email, Slack (team alerts), Zoom (sales call).

## How to use this skill
When the user asks something like *"how do I follow up with this person"*, *"how do I reach out"*, *"how do I get them booked in"*, or *"what am I missing"*:
1. **Locate the stage.** From the prospect's situation, find which box they're in using the Routing map below.
2. **Answer from that box.** Give its Goal, Channels, Automation, and SOP steps — those are the prescribed actions. Don't invent steps that aren't in the funnel; if something genuinely isn't covered, say so.
3. **Respect the timing.** Each box has a trigger/timing rule — don't advise acting earlier than it allows.
4. **Flag gaps.** If the user is skipping a step the box defines (e.g. chasing by phone before the conditional allows, or missing the access-check), point it out.
5. **Mind contact load.** Every WhatsApp/call must carry a *new* reason — the funnel allows up to ~5 WhatsApps across a journey, but only because each has a distinct job. Don't stack same-message pings.

## Channel principles
- Match channel cost to action value. Retargeting ads = opt-in only. Phone reserved for where intent is shown or someone's gone quiet. SMS ~4p/msg (UK, via GHL).
- Speed-to-lead is the highest-impact lever: the opt-in instant WhatsApp (60s) + 15-min call are deliberate and must not be dropped.
- Conditional SOP steps only fire if an earlier contact gets no reply.
- AI/automation stays invisible to the prospect — sell outcomes, never the mechanism.

## Routing map (how stages connect)
```
Opt-in ─ no purchase ─▶ No purchase [END]
       └ purchased ──▶ Purchased course
Purchased course ─▶ Got access · watched ─┬ booked ─▶ Call booked
                                          └ didn't book ─▶ Didn't book [END]
                 ─▶ Got access · didn't watch ─┬ booked ─▶ Call booked
                                               └ didn't book ─▶ Didn't book [END]
                 ─▶ Didn't get access ─┬ booked ─▶ Call booked
                                       └ didn't book ─▶ Didn't book [END]
Call booked ─ no show ─▶ No show [END]
            └ shows up ─▶ Call happens
Call happens ─▶ Closed ─▶ Onboarding [END]
             ─▶ Didn't close · follow-up booked [END]
             ─▶ Didn't close · follow-up NOT booked [END]
```

## Stages & boxes

### Opt-in  *(stage)*
**Goal:** Get them to purchase the low-ticket course.
**Channels:** Phone · Email · SMS · WhatsApp · Retargeting ads

**Automation:**
1. Email sent to prospect
2. SMS sent to prospect
3. Prospect's contact details added to retargeting ads list
4. Email notification sent to Ross (dedicated opt-in inbox, pops up on phone)

**SOP (manual):**
1. WhatsApp prospect within 60 seconds of opt-in
2. Call prospect 15 minutes after opt-in

### No purchase  *(outcome)*
**Trigger / timing:** Automation & SOP trigger no earlier than 24 hours after opt-in
**Goal:** Get them to purchase the course and book a call. If there's friction with the purchase but not with booking, get them booked in for a call without the purchase.
**Channels:** Phone · Email · WhatsApp

**Automation:**
1. Automated email sent to prospect

**SOP (manual):**
1. If there was no response from the Opt-in phone call or WhatsApp → call them
2. If we called but no answer → WhatsApp them
3. If we called and they answered → don't WhatsApp them

### Purchased course  *(stage)*
**Goal:** Get them to watch the course and book a call.
**Channels:** Email · SMS · WhatsApp

**Automation:**
1. Automated email sent to prospect (purchase confirmation + access instructions)
2. Automated SMS sent to prospect (purchase confirmation + access instructions)
3. Zapier auto-invites prospect to Skool with course access granted — prospect clicks 'Join Now' in the Skool invite email to activate
4. Slack channel notification to team (new purchase)

**SOP (manual):**
1. WhatsApp the prospect 2 hours after purchase to check they got access — guide them through if not

### Got access · watched  *(outcome)*
**Goal:** Get them booked in for a call.
**Channels:** —

**Automation:**
- none

**SOP (manual):**
- none
> _Intentionally minimal: a watched + booked lead needs no action; the work lives in the 'Didn't book' box beneath._

### Didn't book — Got access · watched  *(outcome)*
**Trigger / timing:** Triggers 24 hours after Lesson 1 is marked complete — only if no call has been booked
**Goal:** Get them to book a call.
**Channels:** Email · SMS · WhatsApp · Phone

**Automation:**
1. Automated email sent to prospect (booking link)
2. Automated SMS sent to prospect (booking link)

**SOP (manual):**
1. WhatsApp the prospect referencing the course they watched
2. If no reply → call them

### Got access · didn't watch  *(outcome)*
**Trigger / timing:** Triggers 24 hours after access — only if Lesson 1 isn't marked complete
**Goal:** Get them to watch the course.
**Channels:** Email · SMS · WhatsApp

**Automation:**
1. Automated email sent to prospect (reminder to watch + link to Lesson 1)
2. Automated SMS sent to prospect (reminder to watch + link to Lesson 1)

**SOP (manual):**
1. WhatsApp the prospect to nudge them to watch the course

### Didn't book — Got access · didn't watch  *(outcome)*
**Trigger / timing:** Triggers 48 hours after access — only if Lesson 1 isn't complete and no call has been booked
**Goal:** Plan A: get them to watch the course and book a call. Plan B: if watching fails, at least get them to book a call.
**Channels:** Email · SMS · WhatsApp · Phone

**Automation:**
1. Automated email sent to prospect (link to Lesson 1 + booking link)
2. Automated SMS sent to prospect (link to Lesson 1 + booking link)

**SOP (manual):**
1. WhatsApp the prospect to nudge them to watch and book
2. If no reply → call them
3. On the call, push to watch + book; if they won't watch, get the call booked anyway

### Didn't get access  *(outcome)*
**Trigger / timing:** Triggers 4 hours after purchase — only if they haven't activated access (clicked 'Join Now')
**Goal:** Get them access.
**Channels:** Email · SMS · WhatsApp · Phone

**Automation:**
1. Automated email sent to prospect (flags the access issue + re-sends the Skool 'Join Now' invite link)
2. Automated SMS sent to prospect (re-sends the join link)

**SOP (manual):**
1. WhatsApp the prospect to check what went wrong with access and walk them in
2. If no reply → call them and get them in live (talk them through clicking Join)

### Didn't book — Didn't get access  *(outcome)*
**Trigger / timing:** Triggers 24 hours after purchase — only if no call has been booked
**Goal:** Get them to book a call.
**Channels:** Email · SMS · WhatsApp

**Automation:**
1. Automated email sent to prospect (booking link)
2. Automated SMS sent to prospect (booking link)

**SOP (manual):**
1. WhatsApp the prospect to get them to book

### Call booked  *(stage)*
**Goal:** Screen the prospect first — how qualified they are, what angle to take, and whether to take the call at all. Then get them to show up having gone through the pre-call material.
**Channels:** Phone · Email · SMS · WhatsApp

**Automation:**
1. Booking confirmation email
2. SMS confirmation
3. Slack notification to team of new booking

**SOP (manual):**
1. Screen the prospect from their booking-form answers — qualify, pick the angle, decide keep / reschedule / decline
2. WhatsApp a personal confirmation ahead of the call
3. Check they've gone through the pre-call material; nudge if not

### No show  *(outcome)*
**Trigger / timing:** Automation triggers ~15 minutes after the missed call time
**Goal:** Get them to respond, figure out why they didn't show, and get them booked back in.
**Channels:** Phone · Email · SMS · WhatsApp

**Automation:**
1. Automated 'missed you' email sent to prospect (rebooking link)
2. Automated SMS sent to prospect (rebooking link)
3. Slack notification to team of the no-show

**SOP (manual):**
1. WhatsApp the prospect to find out what happened and get them rebooked
2. If no reply → call them
3. Once you reach them, get the call rebooked

### Call happens  *(stage)*
**Goal:** Get them to make a clear decision on the call — to buy or not.
**Channels:** Zoom

**Automation:**
- none

**SOP (manual):**
1. Follow the sales call script

### Closed  *(win)*
**Goal:** Get them onboarded in the best way possible and as fast as possible.
**Channels:** Email

**Automation:**
- none

**SOP (manual):**
- none

### Didn't close follow-up booked  *(outcome)*
**Goal:** Confirm the objection, find a way to overcome it, and prepare for the follow-up call.
**Channels:** Email · SMS · WhatsApp

**Automation:**
1. Follow-up call confirmation email (date/time + Zoom link)
2. SMS confirmation
3. Slack notification to team — didn't close + follow-up booked

**SOP (manual):**
1. Immediately after the call: log why they didn't close and the exact objection
2. Work out how to overcome the objection; prepare the angle + material for the follow-up call
3. Send a resource that pre-handles the objection (case study / proof)
4. WhatsApp a personal touch before the follow-up to keep them warm and confirm they'll show

### Didn't close follow-up NOT booked  *(outcome)*
**Goal:** Find out exactly what the objection was, work out how to overcome it, and get them booked back in for a call.
**Channels:** Email · SMS · WhatsApp

**Automation:**
1. Automated re-engagement email sent to prospect (rebooking link)
2. Automated SMS sent to prospect (rebooking link)
3. Slack notification to team — didn't close + follow-up NOT booked

**SOP (manual):**
1. Immediately after the call: log why they didn't close and the exact objection
2. Work out how to overcome the objection; prepare the angle + material
3. Send a resource that pre-handles the objection (case study / proof)
4. WhatsApp the prospect to re-open the conversation and get the call rebooked

### Onboarding  *(stage)*
**Goal:** Give them the smoothest process possible to minimise the chance of backing out or asking for a refund.
**Channels:** Email

**Automation:**
- none

**SOP (manual):**
- none

## The 16 prospect journeys
Every distinct path a prospect can take (see touchpoints page for contact-load per path):

1. Opt-in → No purchase
2. Opt-in → Purchased → Got access · watched → Didn't book
3. Opt-in → Purchased → Got access · didn't watch → Didn't book
4. Opt-in → Purchased → Didn't get access → Didn't book
5. Opt-in → Purchased → Got access · watched → booked → Call booked → No show
6. Opt-in → Purchased → Got access · watched → booked → Call booked → shows up → Call happens → Closed → Onboarding
7. Opt-in → Purchased → Got access · watched → booked → Call booked → shows up → Call happens → Didn't close (follow-up booked)
8. Opt-in → Purchased → Got access · watched → booked → Call booked → shows up → Call happens → Didn't close (no follow-up)
9. Opt-in → Purchased → Got access · didn't watch → booked → Call booked → No show
10. Opt-in → Purchased → Got access · didn't watch → booked → Call booked → shows up → Call happens → Closed → Onboarding
11. Opt-in → Purchased → Got access · didn't watch → booked → Call booked → shows up → Call happens → Didn't close (follow-up booked)
12. Opt-in → Purchased → Got access · didn't watch → booked → Call booked → shows up → Call happens → Didn't close (no follow-up)
13. Opt-in → Purchased → Didn't get access → booked → Call booked → No show
14. Opt-in → Purchased → Didn't get access → booked → Call booked → shows up → Call happens → Closed → Onboarding
15. Opt-in → Purchased → Didn't get access → booked → Call booked → shows up → Call happens → Didn't close (follow-up booked)
16. Opt-in → Purchased → Didn't get access → booked → Call booked → shows up → Call happens → Didn't close (no follow-up)

## Key automation facts
- **Skool access is fully hands-off via Zapier:** GHL purchase → Zap auto-invites to Skool with course access granted → prospect clicks 'Join Now' in the Skool invite email to activate. No manual approval. Zapier ~$20/mo (Starter), the zap itself is free; ~1 task per purchase.
- **GHL alone can't reach Skool** (no native integration, Skool has no public inbound webhook for invites) — a connector (Zapier) is required.
- **"Watched" = Lesson 1 marked complete in Skool** (Skool only tracks the completion checkmark, not true watch %). Skool's Zapier 'Lesson Completed' trigger fires this. Trigger point chosen = **Lesson 1** (most binge the rest in one go).
- **No-show / access detection** depends on GHL appointment status and whether 'Join Now' was clicked.

---
_Generated from the live map. Regenerate after any map change to stay in sync._