#!/usr/bin/env python3
"""Builds one page per live email in ./emails from the shared CPT template.
Run: python3 emails/_build.py  (from the map folder)."""
import html, pathlib, datetime

HERE = pathlib.Path(__file__).parent
TPL = (HERE / "_template.html").read_text()

def p(t, mb=20, **kw):
    style = f"margin:0 0 {mb}px 0;"
    if kw.get("bold"): style += " font-weight:700; font-size:17px;"
    if kw.get("quote"): style += " padding-left:14px; border-left:3px solid #5690E1;"
    if kw.get("small"): style += " font-size:14px; color:#4B5A77;"
    return f'<p style="{style}">{t}</p>'

def h(t): return p(t, 12, bold=True)

def btn(label, color="#1E3156"):
    return (f'<table border="0" cellpadding="0" cellspacing="0" role="presentation" style="margin:0 0 32px 0;"><tr>'
            f'<td align="center" style="background-color:{color}; border-radius:6px;">'
            f'<a href="#" style="display:inline-block; padding:14px 28px; font-family:Inter, Arial, sans-serif; font-size:15px; font-weight:700; color:#FFFFFF; text-decoration:none; text-transform:uppercase; letter-spacing:0.5px;">{label}</a>'
            f'</td></tr></table>')

def appt(title):
    return (f'<div style="background:#F4F6FA; border-radius:8px; padding:18px 22px; margin:0 0 24px 0;">'
            f'<p style="margin:0 0 8px 0; font-size:12px; font-weight:700; letter-spacing:.5px; color:#5690E1;">{title}</p>'
            f'<p style="margin:0 0 6px 0; font-weight:700;">{{{{appointment.only_start_date}}}} at<br/>{{{{appointment.start_time}}}}</p>'
            f'<p style="margin:0;">Zoom: <a href="#">{{{{appointment.meeting_location}}}}</a></p></div>')

def sig(line="Ross"):
    return p(line, 8) if line == "Ross" else p(line, 8)

EMAILS = []  # filled below; each: slug, step, n, subject, when, source, body(list of html strings)

def add(slug, step, n, subject, when, source, body):
    EMAILS.append(dict(slug=slug, step=step, n=n, subject=subject, when=when, source=source, body=body))

# ---------------- Call booked ----------------
add("call-booked-1", "Call booked", 1, "Your call is confirmed. Here's what to expect.", "Straight after the call is booked",
    "GoHighLevel automation “Call Booked”, step “Email”", [
    p("Hey {{contact.first_name}},"),
    p("Your call with Ross is locked in. 🚀"),
    appt("YOUR APPOINTMENT"),
    p("Add it to your calendar now. That one step will save you the \"wait, when was that again?\" moment on the day."),
    h("Here's what this call actually is."),
    p("It is not a sales pitch. It is not me trying to talk you into something. It is a diagnostic. I'm going to look at where you are right now, where you want to be, and figure out exactly what is standing between those two things."),
    p("Most people who book this call have been thinking about rent-to-rent for months. They've watched the videos. They understand the concept. They just don't have a system that actually works around their life and their capital position. That is what The Rent-to-Rent Fast Track was built to fix, and that is what we'll be diagnosing on the call."),
    p("So come ready to be honest. Not the polished version of yourself. Just where things actually are right now.", quote=True),
    p("See you on the call,", 8),
    p("<b>Ross</b>", 24),
    '<hr style="border:0; border-top:1px solid #E3E7EF; margin:0 0 16px 0;"/>',
    p('Need to reschedule? <a href="#">Click here.</a>', 0, small=True),
])

add("call-booked-2", "Call booked", 2, "What Sam looked like 3 months before his first deal", "23 hours before the call",
    "GoHighLevel automation “Call Booked”, step “Email 2”", [
    p("Hey {{contact.first_name}},"),
    p("We speak tomorrow. I wanted to send you something before then."),
    p("Sam came to me after spending £25,000 on other trainings over two years. He'd tried every strategy, every company, every approach he'd been taught. On paper he'd done all the right things. But he didn't have a single deal to his name."),
    p("Three months later he secured his first one.", quote=True),
    p("Hear it from Sam himself (2 min):", 12),
    '<p style="margin:0 0 28px 0;"><a href="https://youtu.be/86MRhSWPU_g" target="_blank" style="display:inline-block; text-decoration:none;"><img src="https://img.youtube.com/vi/86MRhSWPU_g/hqdefault.jpg" alt="Sam\'s story - watch the 2 minute video" width="480" style="display:block; width:100%; max-width:480px; height:auto; border-radius:8px; border:0;" /></a><br/><a href="https://youtu.be/86MRhSWPU_g" target="_blank" style="color:#5690E1; font-weight:700;">&#9654; Watch Sam\'s 2 minute video</a></p>',
    p("Not because the information was different. Because he stopped trying to learn more and started executing on a plan built specifically for his situation."),
    p("That is what I want to map out for you."),
    p("Tomorrow I'm going to look at your specific area, your specific capital position, your timeline, and your goals. I'm going to find the one or two things that are actually keeping you stuck and tell you exactly what needs to change."),
    p("You will leave with clarity on what to do, regardless of what you decide after that."),
    p("Come with your honest numbers. Capital available, target area, how long this has been on your mind. The more real you are with me, the more useful I can be."),
    appt("YOUR CALL TOMORROW"),
    p('If something has come up, <a href="#">reschedule here</a>.'),
    p("See you tomorrow.", 8),
    p("<b>Ross</b>", 0),
])

add("call-booked-3", "Call booked", 3, "Your call is in a 2 hours. Read this first.", "2 hours before the call",
    "GoHighLevel automation “Call Booked”, step “Email 3”", [
    p("Hey {{contact.first_name}},"),
    p("A few hours out. I want to make sure you get the most from our time together."),
    h("Three things I want you to do before you join."),
    h("1. Find a quiet space."),
    p("Not the car, not between meetings. Somewhere you can actually talk openly. The people who treat this call like a priority are always the ones who walk away with the most clarity."),
    h("2. Know your numbers."),
    p("What capital do you actually have available right now. What's your target area. How long have you been thinking about starting. You do not need all the answers. Just know the basics before we start."),
    h("3. Drop the performance."),
    p("I speak to people every single day who tell me they're \"mostly ready, just need to tighten things up.\" The ones who get real results from working with me are the ones who show up as they actually are, not as they want to be seen."),
    p("I'm not there to judge where you are. I'm there to help you figure out how to get where you want to be. But that only works if you're straight with me.", quote=True),
    p("Join here:"),
    appt("YOUR CALL TODAY"),
    btn("Join the call"),
    p("See you soon.", 8),
    p("<b>Ross</b>", 0),
])

# ---------------- Purchased course ----------------
add("purchased-2", "Purchased course", 2, "The truth about why you're still stuck ❌", "1 day after purchase",
    "GoHighLevel automation “LT purchased”, step “Email 2”", [
    p("Hey {{contact.first_name}},"),
    p("If you're like most people I speak to, you've watched the YouTube videos. Read the Reddit threads. Maybe even paid for a course or two. You understand the model. You know rent-to-rent works."),
    p("But you still haven't done a single deal."),
    h("Here's why."),
    p("Most people don't have an information problem. They have an architecture problem."),
    p("Take my client Sam."),
    p("He came to me after spending just under £25,000 on other trainings over two years. Different strategies, different companies. He'd tried everything he'd been taught and was getting absolutely nowhere."),
    p("So we stopped trying to learn more. We sat down, looked at his actual situation, his actual area, his actual capital position, and built one specific plan."),
    p("Three months later he signed his first deal."),
    p("Not because the information was different. Because he stopped consuming and started executing on a plan built for him."),
    p("If you're tired of watching property videos and still not having a deal to your name, book your free strategy call below."),
    btn("Book Your Free Strategy Call", "#5690E1"),
    p("Let's stop you from being another year in research mode."),
    p("Ross"),
    p("P.S. The Mortgage Myth Calculator inside the Fast Track takes 10 minutes to run. If you haven't yet, do it tonight. Your area either works or it doesn't, and you should know before the week is out.", 0),
])

add("purchased-3", "Purchased course", 3, "Why landlords say no (and how to make them say yes)", "2 days after purchase",
    "GoHighLevel automation “LT purchased”, step “Email 3”", [
    p("Hey {{contact.first_name}},"),
    p("There's a number most rent-to-rent coaches will never tell you."),
    p('<span style="font-size:28px; font-weight:700;">55.</span>', quote=True),
    p("That's how many calls one of my newer clients made before he secured his first deal. 25 landlords said no immediately. 25 had conversations but weren't ready. 5 said yes. From those 5 conversations, he got his first property."),
    p("Most people try twice and decide the model doesn't work."),
    p("The model works. They just don't understand what the numbers game actually looks like."),
    p("Take Endrit. When he started, he was getting 2 viewings a month. After we worked on his approach together, he was getting 6 to 7 viewings a day."),
    p("Same person. Same market. Completely different conversion."),
    p("What changed wasn't his charm. It was structure. The opening frame. The value proposition in plain English. The three objections every landlord raises and the specific response to each."),
    p("That's all in Lesson 3 of the Fast Track, with the Landlord Yes Formula Preparation Sheet ready to print and use."),
    p("But here's the part the course can't do for you."),
    p("Watching me look at your specific area, your specific landlord sources, and your specific situation, and telling you exactly which landlords to approach first and what to say when you do."),
    p("That's what the strategy call is for."),
    btn("Book Your Strategy Call", "#5690E1"),
    p("Ross"),
    p("P.S. Endrit now has two six-figure businesses. He started where you are now.", 0),
])

add("purchased-4", "Purchased course", 4, "The £15,000 mistake (and how to avoid it)", "3 days after purchase",
    "GoHighLevel automation “LT purchased”, step “Email 4”", [
    p("Hey {{contact.first_name}},"),
    p("Here is something most coaches won't tell you."),
    p("A bad rent-to-rent deal costs £5,000 to £15,000 before you earn a penny. The deposit. The first month's rent. The furniture. The set-up."),
    p("The people who lose money on deal one almost always skipped the numbers. The house \"felt right\"."),
    p("The people still in the game three years on walked away from houses that felt right but failed the numbers."),
    p("Take Mickey."),
    p("His deal should bring in £4,000 to £5,000 a month. Take off £2,050 rent and about £500 in bills. That leaves £1,500 to £2,000 profit a month, from one house."),
    p("That did not come from a hunch. He ran the numbers before he signed."),
    p("Lesson 4 of the Fast Track shows you the exact checks I run on my own deals. The margin test. How many months to get your money back. The £15,000 Mistake Checklist."),
    p("Most people run it on one or two houses and feel sure."),
    p("The ones who scale run it with someone looking over their shoulder for the first few deals. One missed line can turn a good deal into a bad one."),
    p("That is what we do on your free call."),
    btn("Book Your Free 1:1", "#5690E1"),
    p("Ross", 0),
])

add("purchased-5", "Purchased course", 5, "Are you actually going to do this?", "4 days after purchase",
    "GoHighLevel automation “LT purchased”, step “Email 5”", [
    p("Hey {{contact.first_name}},"),
    p("I want to be straight with you."),
    p("You've had The Rent-to-Rent Fast Track for four days now. Eight lessons. Every tool downloadable. The entire 9-year system I've used to manage 30+ properties and help 230+ people land their first deal."),
    p("A week from now you'll either have run the Mortgage Myth Calculator on your area, made your first landlord call, and started executing the 90-Day Deal Roadmap."),
    p("Or you won't."),
    p("That's the honest fork in the road."),
    p("Jorge had it. He took the system, made the calls, signed his first deal in November, and since then he's signed 7 more. It's his full-time job now. He's still scaling."),
    p("His words: \"It's challenging at the beginning, but it's not difficult once you have the right system.\"", quote=True),
    p("You have the system. The question is whether you have someone in your corner who can shorten the gap between where you are and where Jorge is now."),
    p("That's what the strategy call is for. Not a pitch. A real conversation about your area, your capital, your timeline, and the specific first move that makes sense for you."),
    p("I take a limited number of these every week."),
    btn("Book Your Call", "#5690E1"),
    p("See you on the call,", 8),
    p("Ross"),
    p("P.S. If you've decided this isn't for you, just hit reply and let me know. I read every email on this list personally. I'd rather you say so than sit on a system you're never going to use.", 0),
])


# ---------------- plain-text emails (GoHighLevel "quick compose", no template) ----------------
def plain(lines):
    return [p(l) for l in lines]

add("purchased-1", "Purchased course", 1, "The Rent-to-Rent Fast Track Access 🔑", "Straight after purchase",
    "GoHighLevel automation “RTR — Course Access Gate Submitted”, step “Email”", [
    p("Hey {{contact.first_name}},"),
    p("Welcome to The Rent-to-Rent Fast Track. 🚀"),
    p("You're officially in, and you've just made one of the best decisions for your property business."),
    p("<b>Important:</b> your course is in a separate email from Skool. Open it and click <b>\"Join Now\"</b>. That's the only way to unlock it. Please don't join from the Skool website, as that gets you into the group without the course. Can't find it? Check spam, or just reply here."),
    p("Just give us a bit of time to get everything set up on your end. In the meantime, book your free 1:1 property strategy call with me here:"),
    btn("Book Your Free Strategy Call", "#5690E1"),
    h("Here's what you'll walk away with:"),
    p("1. A full audit of your current situation, target area, and capital position.", 12),
    p("2. A custom 90-day plan built around your specific market and constraints.", 12),
    p("3. Clear next steps to land your first profitable rent-to-rent deal.", 28),
    h("This call alone has helped people go from:"),
    p("£25,000 spent on other trainings with zero deals to first deal secured in 3 months. (Sam)", 12, quote=True),
    p("Messy business with 2 viewings a month to two six-figure companies and 6 to 7 viewings a day. (Endrit)", 12, quote=True),
    p("Zero deals to 8 active rent-to-rents and full-time property income. (Jorge)", 28, quote=True),
    p("You're up next."),
    p("See you inside,", 8),
    p("<b>Ross</b>", 0),
])

add("didnt-book-1", "Didn't book", 1, "Your free call is still open", "48 hours after purchase, if no call booked",
    "GoHighLevel automation “Didn't Book — Book Nudge”, step “Email”", plain([
    "Hi {{contact.first_name}},",
    "You've got the Fast Track. The call is where it gets built around you.",
    "On the call we look at where you are now, where you want to be, and put a plan together for your first deal.",
    "It's free. It came with your purchase.",
    "Pick a time in the next three days — that's as far ahead as my calendar opens.",
    '<a href="#"><b>Book my free call</b></a>',
    "Talk soon,",
    "Ross",
]))

add("didnt-watch-1", "Got access · didn't watch", 1, "You're in, here's where to start", "9 am UK, at least 24 hours after unlocking the course — skipped if they've started watching",
    "GoHighLevel automation “Got Access — Didn't Watch”, step “Email”", plain([
    "Hi {{contact.first_name}},",
    "You've got full access to The Rent-to-Rent Fast Track.",
    "The welcome video is where it clicks. It walks you through how the model actually works, so you can spot your first deal instead of guessing. Most people get through it in one sitting, and at the end it shows you exactly how to book your call with me.",
    "To start, open the Skool invite email we sent you (check spam) and tap Join Now. That opens your course.",
    "Any trouble getting in, just reply to this email and I'll sort it.",
    "Ross Cheung",
]))

add("didnt-watch-2", "Got access · didn't watch", 2, "Your Fast Track is waiting for you", "4 days after Email 1 (about day 5) — skipped if they've started watching",
    "GoHighLevel automation “Got Access — Didn't Watch”, step “Email 2”", plain([
    "Hi {{contact.first_name}},",
    "You bought The Rent-to-Rent Fast Track a few days ago, and it looks like you haven't been able to get started yet.",
    "I don't want you to miss out on what you paid for. Inside is the exact process for finding your first rent-to-rent deal — the thing that gets you your first income without buying a property. It's all there, ready when you are.",
    "Here's your link again so you don't have to dig for it: <a href=\"#\">Open the Fast Track</a>",
    "And if the problem is getting in — invite didn't arrive, landed in spam, wrong email — just reply and I'll sort it for you today. That's what I'm here for.",
    "Ross Cheung",
]))

add("didnt-watch-3", "Got access · didn't watch", 3, "Your Fast Track is still waiting for you", "9 days after Email 2 (about day 14) — skipped if they've started watching",
    "GoHighLevel automation “Got Access — Didn't Watch”, step “Email 3”", plain([
    "Hi {{contact.first_name}},",
    "You bought The Rent-to-Rent Fast Track a couple of weeks ago, and it looks like you haven't been able to get started yet.",
    "I don't want you to miss out on what you paid for. Inside is the exact process for finding your first rent-to-rent deal — the thing that gets you your first income without buying a property. It's all there, ready when you are.",
    "Here's your link again so you don't have to dig for it: <a href=\"#\">Open the Fast Track</a>",
    "And if the problem is getting in — invite didn't arrive, landed in spam, wrong email — just reply and I'll sort it for you today. That's what I'm here for.",
    "Ross Cheung",
]))

add("no-access-1", "Didn't get access", 1, "I've re-sent your Fast Track access", "48 hours and 7 days after purchase, if still not in Skool",
    "GoHighLevel automation “Fast Track - Skool Invite Re-sent (48h / 7d)”, step “Email”", plain([
    "Hi {{contact.first_name}},",
    "I noticed you haven't got into your Rent-to-Rent Fast Track yet, so I've just re-sent your invite.",
    'Look for the email from Skool (check spam too) and click "Join Now". That takes you straight into the course.',
    "If you'd rather use a different email address for Skool, just reply here and tell me which one. I'll send the invite there.",
    "Ross",
]))

add("no-show-1", "No show", 1, "Missed you, let's get you rebooked", "When the booking is marked as a no-show",
    "GoHighLevel automation “No Show — Rebook”, step “Email”", plain([
    "Hi {{contact.first_name}},",
    "Looks like we missed each other for your Rent-to-Rent strategy call, no worries, it happens.",
    "Let's get you back in. Pick a new time that works and we'll carry on where we left off:",
    '<a href="#">https://api.leadconnectorhq.com/widget/booking/QFXxD77UuuApYnPl0Y0V</a>',
    "Speak soon,",
    "Ross Cheung",
]))

add("dc-booked-1", "Didn't close · follow-up booked", 1, "Looking forward to our follow-up", "When the card moves to “Call Completed – Follow-up”",
    "GoHighLevel automation “Didn't Close — Follow-up Booked”, step “Email”", plain([
    "Hi {{contact.first_name}},",
    "Great speaking with you. Your follow-up call is booked and I'm looking forward to picking things back up.",
    "Before then, have a think about anything still on your mind. We'll work through it together and get you a clear plan.",
    "Speak soon,",
    "Ross Cheung",
]))

add("dc-not-1", "Didn't close · follow-up NOT booked", 1, "Picking up where we left off", "When the card moves to “Deal Lost”",
    "GoHighLevel automation “Didn't Close — No Follow-up”, step “Email”", plain([
    "Hi {{contact.first_name}},",
    "It was good speaking with you about your Rent-to-Rent plans. I know the timing wasn't quite right to move forward on our call, but I didn't want to leave it there.",
    "If you're still serious about landing your first deal, let's get another time in and map out how to make it happen:",
    '<a href="#">https://api.leadconnectorhq.com/widget/booking/QFXxD77UuuApYnPl0Y0V</a>',
    "Speak soon,",
    "Ross Cheung",
]))


add("onboarding-1", "Onboarding", 1, "Welcome to Capital Property Training, {{contact.first_name}} – your next steps", "About 1 minute after the card is moved to Closed - Won",
    "Zapier automation “cpt-client-onboarding”, step “Welcome email” (sent from ross@capitalpropertytraining.com as Ross Cheung)", [
    p("Hi {{contact.first_name}},"),
    p("Welcome aboard. Great call today, and well done for backing yourself."),
    p("You'll also get a separate email from me with your coaching agreement. Please read it and sign it — it only takes a minute on your phone."),
    h("What you've signed up for:"),
    p("Full one-to-one support from me until your rent-to-rent business is making £10,000 net profit a month."),
    h("Your folder:"),
    p('Everything you need is in one place here: <a href="#">[Folder Link]</a>'),
    p("Inside you'll find your 90-Day Plan, your Success Benchmarks tracker, your Operating Sheet, your market research sheet, your deal calculator and your marketing templates."),
    h("Your courses:"),
    p("I've given you access to my courses on Skool. Log in and you'll find them waiting for you. Feel free to start going through them before our first call."),
    h("How it works:"),
    p("<b>1. Onboarding call</b><br/>I'll send you a calendar invite with a Zoom link. On the call I'll walk you through the programme and ask you about your goals, money to invest, area and time."),
    p("<b>2. Your plan</b><br/>We'll go through your 90-Day Plan and Success Benchmarks together, so you know exactly what to do from day one."),
    p("<b>3. From there</b><br/>You work through your benchmarks, and we get on a call at the key ones to plan what's next."),
    h("Before our first call, please:"),
    p("- Sign your coaching agreement (in the separate email).<br/>- Have a think about how much you can invest and which area you'd like to work in."),
    p("If you need me, WhatsApp me on 07940 224276."),
    p("Speak soon.", 8),
    p("Ross<br/>Capital Property Training", 0),
])

# ---------------- SMS (text messages to the prospect) ----------------
SMS = []
def sms(slug, step, when, source, text):
    SMS.append(dict(slug=slug, step=step, when=when, source=source, text=text))

BOOK = "https://api.leadconnectorhq.com/widget/bookings/rent-to-rent-strategy-playbook"

sms("sms-purchased-1", "Purchased course", "Straight after purchase",
    "GoHighLevel automation “RTR — Course Access Gate Submitted”, step “SMS”",
    "{{contact.first_name}}, you're in — thanks for grabbing the rent2rent fasttracker. check your email for the skool invite and hit 'join now' to unlock lesson 1.")

sms("sms-didnt-watch-1", "Got access · didn't watch", "9 am UK, at least 24 hours after unlocking the course — straight after Email 1; skipped if they've started watching",
    "GoHighLevel automation “Got Access — Didn't Watch”, step “SMS”",
    "{{contact.first_name}}, you're in but haven't started the Fast Track yet. It shows how rent-to-rent works without buying property. To jump into lesson 1, open the Skool invite email we sent you (check spam) and tap Join Now. That opens your course.")

sms("sms-no-access-1", "Didn't get access", "48 hours and 7 days after purchase, if still not in Skool — same moment as the invite re-send",
    "GoHighLevel automation “Fast Track - Skool Invite Re-sent (48h / 7d)”, step “SMS”",
    "Hi {{contact.first_name}}, Ross here. I noticed you haven't got into your Rent-to-Rent Fast Track yet, so I've just re-sent your invite email from Skool. Tap \"Join Now\" in that email and you'll go straight into the course.")

sms("sms-didnt-book-1", "Didn't book", "72 hours after purchase, if no call booked (24 hours after Email 1)",
    "GoHighLevel automation “Didn't Book — Book Nudge”, step “SMS”",
    "{{contact.first_name}}, glad you got through the course. next step's your free call — i'll build out a business plan for your situation. grab a slot: " + BOOK)

sms("sms-call-booked-1", "Call booked", "Straight after the call is booked",
    "GoHighLevel automation “Call Booked”, step “SMS”",
    "{{contact.first_name}}, you're booked in for {{appointment.start_date_time}} — looking forward to it. go through the training first so we can build your plan on the call: open the Skool invite email we sent you (check spam) and tap Join Now. That opens your course.")

sms("sms-no-show-1", "No show", "15 minutes after the booking is marked no-show (Email 1 goes first)",
    "GoHighLevel automation “No Show — Rebook”, step “SMS”",
    "{{contact.first_name}}, had you down for a call just now and we missed each other — everything ok? grab a new slot and we'll pick it up: " + BOOK)

sms("sms-dc-booked-1", "Didn't close · follow-up booked", "1 minute after the card is moved to Call Completed-Follow UP",
    "GoHighLevel automation “Didn't Close — Follow-up Booked”, step “SMS”",
    "{{contact.first_name}}, follow-up's locked in for {{appointment.start_date_time}} — sent you something to watch before then that covers what we discussed. see you then; your zoom link's in the calendar invite.")

sms("sms-dc-not-1", "Didn't close · follow-up NOT booked", "1 hour after the card is moved to Deal Lost",
    "GoHighLevel automation “Didn't Close — No Follow-up”, step “SMS”",
    "{{contact.first_name}}, been thinking about what you raised on the call — reckon i can show you a way through it. grab a quick slot and we'll go through it properly: " + BOOK)

# ---------------- WhatsApp (manual, sent by Ross) ----------------
WA_PAGE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>WhatsApp — Purchased course</title>
<style>
 body{{margin:0;background:#0f1117;color:#e7e9ee;font-family:-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif}}
 .bar{{background:#161922;border-bottom:2px solid #191970;padding:12px 18px;display:flex;flex-wrap:wrap;gap:8px 22px;align-items:center;font-size:13px}}
 .bar a{{color:#9fb0ff;text-decoration:none;font-weight:700}}
 .bar b{{color:#fff}}
 .meta{{color:#9aa0ad}}
 .note{{max-width:420px;margin:18px auto 10px;padding:0 12px;font-size:12px;color:#9aa0ad}}
 .phone{{max-width:420px;margin:0 auto 40px;background:#efe7dd;border-radius:28px;padding:22px 14px 30px;box-shadow:0 0 0 8px #22252f}}
 .from{{text-align:center;color:#6b7280;font-size:12px;margin:0 0 14px}}
 .b{{background:#dcf8c6;color:#111;border-radius:12px;padding:9px 12px;font-size:15.5px;line-height:1.4;max-width:86%;margin:0 0 8px auto;box-shadow:0 1px 0 rgba(0,0,0,.08);white-space:pre-wrap}}
 .vid{{background:#dcf8c6;border-radius:12px;padding:8px;max-width:86%;margin:0 0 8px auto;box-shadow:0 1px 0 rgba(0,0,0,.08)}}
 .vid .box{{background:#111;border-radius:8px;height:170px;display:flex;align-items:center;justify-content:center;color:#fff;font-size:14px}}
 .t{{display:block;text-align:right;font-size:11px;color:#667;margin-top:4px}}
</style></head><body>
<div class="bar">
  <a href="../index.html">← Back to map</a>
  <span><span class="meta">Step:</span> <b>Purchased course</b></span>
  <span><span class="meta">WhatsApp — sent by Ross by hand</span></span>
  <span><span class="meta">Sent:</span> <b>Within a minute of purchase, after the purchase alert</b></span>
</div>
<div class="note">Copied from a real WhatsApp thread on {date}. Ross sends this himself from his phone; it is not automated.</div>
<div class="phone"><div class="from">WhatsApp · from Ross</div>
<div class="b">Hi [first name]<span class="t">00:28</span></div>
<div class="vid"><div class="box">▶ Welcome video (recorded for them)</div><span class="t">00:28</span></div>
<div class="b">Really excited to have you here. I recorded this personally for you - check it out<span class="t">00:28</span></div>
<div class="b">Your onboarding call is included in your purchase - but you only have 72 hours to book it. Want me to lock in a time for you?<span class="t">00:28</span></div>
</div>
</body></html>"""

sms("sms-ross-purchase-alert", "Purchased course", "Straight after purchase — to Ross, not the prospect (then the phone rings up to 6 times, 30 seconds apart: “New sale. [name]. Check your texts.”)",
    "Make automation “Purchase Alert - Call Ross”, step “Send SMS” (from the Twilio number)",
    "NEW CPT SALE\nName: {{full_name}}\nPhone: {{phone}}\nPaid: £{{amount}} - {{product}}\nWhatsApp: https://wa.me/{{phone digits}}")

SMS_PAGE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>
 body{{margin:0;background:#0f1117;color:#e7e9ee;font-family:-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif}}
 .bar{{background:#161922;border-bottom:2px solid #191970;padding:12px 18px;display:flex;flex-wrap:wrap;gap:8px 22px;align-items:center;font-size:13px}}
 .bar a{{color:#9fb0ff;text-decoration:none;font-weight:700}}
 .bar b{{color:#fff}}
 .meta{{color:#9aa0ad}}
 .note{{max-width:420px;margin:18px auto 10px;padding:0 12px;font-size:12px;color:#9aa0ad}}
 .phone{{max-width:420px;margin:0 auto 40px;background:#fff;border-radius:28px;padding:22px 16px 30px;box-shadow:0 0 0 8px #22252f}}
 .from{{text-align:center;color:#6b7280;font-size:12px;margin:0 0 14px}}
 .bubble{{background:#e9e9eb;color:#111;border-radius:18px;padding:12px 14px;font-size:16px;line-height:1.4;max-width:88%;white-space:pre-wrap;word-wrap:break-word}}
 .bubble .mf{{background:#dbe4ff;color:#1E3156;border-radius:4px;padding:0 4px;font-size:14px}}
 .bubble a{{color:#1d4ed8;pointer-events:none}}
</style></head><body>
<div class="bar">
  <a href="../index.html">← Back to map</a>
  <span><span class="meta">Step:</span> <b>{step}</b></span>
  <span><span class="meta">Text message</span></span>
  <span><span class="meta">Sent:</span> <b>{when}</b></span>
</div>
<div class="note">Copied from {source} on {date}. Links are switched off on this copy. Highlighted parts are filled in per person.</div>
<div class="phone"><div class="from">Text Message · from Capital Property Training</div><div class="bubble">{text}</div></div>
</body></html>"""

import re
def render_sms_text(t):
    t = html.escape(t)
    t = re.sub(r"\{\{([^}]+)\}\}", r'<span class="mf">\1</span>', t)
    t = re.sub(r"(https?://\S+)", r'<a href="#">\1</a>', t)
    return t

# ---------------- WhatsApp (automated, from the GoHighLevel line) ----------------
WA_AUTO = []
def wa(slug, step, when, template, text):
    WA_AUTO.append(dict(slug=slug, step=step, when=when, template=template, text=text))

wa("whatsapp-didnt-book-2", "Didn’t book", "12:30 pm UK the day after the first call, only if still not booked (GoHighLevel automation “Call List — not booked (3 tries)”)",
   "didnt_book_day2",
   "Hi {{first name}}. What area are you looking at for your first deal? Send me the town and I'll pull some rent numbers together for you before we speak on your free call.")
wa("whatsapp-didnt-book-3", "Didn’t book", "12:30 pm UK the day after that, only if still not booked — last one, then the card goes to Deal Lost",
   "didnt_book_day3",
   "Hi {{first name}}, it's Ross. Last one from me. I'm starting to feel like that mate who keeps asking you to come to the gym. Your free call is still there if you want it. Just reply YES and I'll send you two times.")

WA_AUTO_PAGE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>
 body{{margin:0;background:#0f1117;color:#e7e9ee;font-family:-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif}}
 .bar{{background:#161922;border-bottom:2px solid #191970;padding:12px 18px;display:flex;flex-wrap:wrap;gap:8px 22px;align-items:center;font-size:13px}}
 .bar a{{color:#9fb0ff;text-decoration:none;font-weight:700}}
 .bar b{{color:#fff}}
 .meta{{color:#9aa0ad}}
 .note{{max-width:420px;margin:18px auto 10px;padding:0 12px;font-size:12px;color:#9aa0ad}}
 .phone{{max-width:420px;margin:0 auto 40px;background:#efe7dd;border-radius:28px;padding:22px 14px 30px;box-shadow:0 0 0 8px #22252f}}
 .from{{text-align:center;color:#6b7280;font-size:12px;margin:0 0 14px}}
 .b{{background:#dcf8c6;color:#111;border-radius:12px;padding:9px 12px;font-size:15.5px;line-height:1.4;max-width:86%;margin:0 0 8px auto;box-shadow:0 1px 0 rgba(0,0,0,.08);white-space:pre-wrap}}
 .b .mf{{background:#dbe4ff;color:#1E3156;border-radius:4px;padding:0 4px;font-size:14px}}
 .t{{display:block;text-align:right;font-size:11px;color:#667;margin-top:4px}}
</style></head><body>
<div class="bar">
  <a href="../index.html">← Back to map</a>
  <span><span class="meta">Step:</span> <b>{step}</b></span>
  <span><span class="meta">WhatsApp — sent automatically from the Capital Property Training line (07414 215073)</span></span>
  <span><span class="meta">Sent:</span> <b>{when}</b></span>
</div>
<div class="note">Meta-approved template “{template}”, copied on {date}. Highlighted parts are filled in per person. If they reply, the chase stops and Ross answers from the GoHighLevel inbox.</div>
<div class="phone"><div class="from">WhatsApp · from Ross Cheung</div>
<div class="b">{text}<span class="t">12:30</span></div>
</div>
</body></html>"""

# ---------------- call script (Ross, by phone) ----------------
SCRIPT_PAGE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Call script — Didn’t book</title>
<style>
 body{{margin:0;background:#0f1117;color:#e7e9ee;font-family:-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif}}
 .bar{{background:#161922;border-bottom:2px solid #191970;padding:12px 18px;display:flex;flex-wrap:wrap;gap:8px 22px;align-items:center;font-size:13px}}
 .bar a{{color:#9fb0ff;text-decoration:none;font-weight:700}}
 .bar b{{color:#fff}}
 .meta{{color:#9aa0ad}}
 .wrap{{max-width:560px;margin:0 auto;padding:18px 16px 60px}}
 .note{{font-size:12px;color:#9aa0ad;margin:0 0 18px}}
 .say{{background:#1b1f2a;border-left:4px solid #9fb0ff;border-radius:0 12px 12px 0;padding:14px 16px;font-size:19px;line-height:1.45;margin:0 0 14px}}
 .say .fill{{background:#dbe4ff;color:#1E3156;border-radius:4px;padding:0 5px}}
 .say .cue{{color:#9aa0ad;font-size:15px}}
 .do{{font-size:15px;color:#cfd3dc;margin:4px 0 18px;padding-left:4px}}
 h3{{font-size:13px;letter-spacing:.06em;text-transform:uppercase;color:#9aa0ad;margin:26px 0 8px}}
 ul{{margin:0;padding-left:20px;font-size:15px;line-height:1.6;color:#cfd3dc}}
</style></head><body>
<div class="bar">
  <a href="../index.html">← Back to map</a>
  <span><span class="meta">Step:</span> <b>Didn’t book</b></span>
  <span><span class="meta">Phone call — Ross rings them</span></span>
  <span><span class="meta">When:</span> <b>24 h after purchase (6 pm UK), then 12:30 pm UK the next two days</b></span>
</div>
<div class="wrap">
<div class="note">Approved {date}. Slow, calm, like someone they already know. Pause where it says. Highlighted parts change per person.</div>

<div class="say"><span class="fill">[First name]</span>?… <span class="cue">(pause)</span> …It’s Ross, Ross Cheung from Capital Property Training.</div>

<div class="say">You grabbed the Rent-to-Rent Fast Track <span class="fill">[yesterday / a couple of days ago]</span>, and that came with a free call with me. I saw you hadn’t put a time in, so I thought I’d ring you myself.</div>

<div class="say">I’ve only got a couple of minutes before my next call, but… it’s just looking at where you’re at now, where you want to be, and helping you put a plan together.</div>

<div class="say">Are you already investing in property, or are you looking to just get started?</div>

<div class="say">How long have you been thinking about doing something like this?</div>

<div class="say">Okay. If I was to spare some time for a call to create a plan with you, would that be helpful? <span class="cue">(wait)</span></div>

<div class="say">I’ve got my calendar open — <span class="fill">[Day, time]</span> or <span class="fill">[Day, time]</span>?</div>

<div class="do">Book it while they’re on the line. Confirm number and email.</div>

<div class="say">Zoom link’s on its way by text and email.</div>

<h3>No answer</h3>
<ul><li>Ring twice, back to back.</li><li>Then the Day-1 text.</li><li>Try again at the next slot.</li></ul>

<h3>Don’t say</h3>
<ul><li>“How’s your day?”</li><li>“Thanks for buying”</li><li>Credentials (“I’ve done 30 units…”)</li><li>“Book you in” — say “grab a slot”</li><li>Anything after a question until they answer</li></ul>
</div>
</body></html>"""

# ---------------- page writer ----------------
PAGE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>
 body{{margin:0;background:#0f1117;color:#e7e9ee;font-family:-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif}}
 .bar{{background:#161922;border-bottom:2px solid #191970;padding:12px 18px;display:flex;flex-wrap:wrap;gap:8px 22px;align-items:center;font-size:13px}}
 .bar a{{color:#9fb0ff;text-decoration:none;font-weight:700}}
 .bar b{{color:#fff}}
 .meta{{color:#9aa0ad}}
 .frame{{padding:18px 0 40px}}
 .note{{max-width:600px;margin:0 auto 10px;padding:0 12px;font-size:12px;color:#9aa0ad}}
</style></head><body>
<div class="bar">
  <a href="../index.html">← Back to map</a>
  <span><span class="meta">Step:</span> <b>{step}</b></span>
  <span><span class="meta">Email {n}</span></span>
  <span><span class="meta">Sent:</span> <b>{when}</b></span>
  <span><span class="meta">Subject:</span> <b>{subject}</b></span>
</div>
<div class="frame">
  <div class="note">Copied from {source} on {date}. Buttons and links are switched off on this copy.</div>
  {email}
</div>
</body></html>"""

def build():
    today = datetime.date.today().strftime("%-d %b %Y")
    for e in EMAILS:
        email_html = TPL.replace("{{BODY}}", "\n".join(e["body"]))
        out = PAGE.format(title=f"Email {e['n']} — {e['step']}", step=html.escape(e["step"]), n=e["n"],
                          when=html.escape(e["when"]), subject=html.escape(e["subject"]),
                          source=html.escape(e["source"]), date=today, email=email_html)
        (HERE / f"{e['slug']}.html").write_text(out)
        print("wrote", e["slug"])
    for m in SMS:
        out = SMS_PAGE.format(title=f"Text — {m['step']}", step=html.escape(m["step"]),
                              when=html.escape(m["when"]), source=html.escape(m["source"]),
                              date=today, text=render_sms_text(m["text"]))
        (HERE / f"{m['slug']}.html").write_text(out)
        print("wrote", m["slug"])
    (HERE / "whatsapp-purchased.html").write_text(WA_PAGE.format(date=today))
    print("wrote whatsapp-purchased")
    (HERE / "script-didnt-book.html").write_text(SCRIPT_PAGE.format(date=today))
    print("wrote script-didnt-book")
    for m in WA_AUTO:
        out = WA_AUTO_PAGE.format(title=f"WhatsApp — {m['step']}", step=html.escape(m["step"]),
                                  when=html.escape(m["when"]), template=html.escape(m["template"]),
                                  date=today, text=render_sms_text(m["text"]))
        (HERE / f"{m['slug']}.html").write_text(out)
        print("wrote", m["slug"])

if __name__ == "__main__":
    build()
