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
    p("P.S. The Mortgage Myth Calculator inside the playbook takes 10 minutes to run. If you haven't yet, do it tonight. Your area either works or it doesn't, and you should know before the week is out.", 0),
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
    p("That's all in Lesson 3 of the playbook, with the Landlord Yes Formula Preparation Sheet ready to print and use."),
    p("But here's the part the playbook can't do for you."),
    p("Watching me look at your specific area, your specific landlord sources, and your specific situation, and telling you exactly which landlords to approach first and what to say when you do."),
    p("That's what the strategy call is for."),
    btn("Book Your Strategy Call", "#5690E1"),
    p("Ross"),
    p("P.S. Endrit now has two six-figure businesses. He started where you are now.", 0),
])

add("purchased-4", "Purchased course", 4, "The £15,000 mistake (and how to avoid it)", "3 days after purchase",
    "GoHighLevel automation “LT purchased”, step “Email 4”", [
    p("Hey {{contact.first_name}},"),
    p("I want to tell you something most coaches won't."),
    p("A bad rent-to-rent deal will cost you between £5,000 and £15,000 out of pocket before you've earned a single pound. The deposit. The first month's rent to the landlord. The furnishing. The setup. Maybe a protracted exit negotiation if the numbers don't hold up."),
    p("The operators who lose money on their first deal are almost always the ones who skipped the analysis because the property \"felt right.\""),
    p("The operators who are still in the business three years later are the ones who walked away from properties that felt right but didn't pass the numbers."),
    p("Take Mickey."),
    p("He's expecting around £4,000 to £5,000 in revenue from his deal. Minus £2,050 rent, minus around £500 in bills. That leaves £1,500 to £2,000 in profit a month, every month, from one property."),
    p("That number didn't come from a hunch. It came from running the calculations before he signed anything."),
    p("Lesson 4 inside the playbook walks you through the exact deal analysis I run on my own portfolio. The margin test. The months-to-recoup calculation. The £15,000 Mistake Checklist."),
    p("Most people run it on one or two properties and feel confident."),
    p("The ones who actually scale run it with someone looking over their shoulder for the first few deals, because the difference between a good number and a great number on paper is often a single line item most beginners miss."),
    p("That's what we do on the strategy call."),
    btn("Book Your Free 1:1", "#5690E1"),
    p("Ross", 0),
])

add("purchased-5", "Purchased course", 5, "Are you actually going to do this?", "4 days after purchase",
    "GoHighLevel automation “LT purchased”, step “Email 5”", [
    p("Hey {{contact.first_name}},"),
    p("I want to be straight with you."),
    p("You've had The Rent-to-Rent Fast Track for a week now. Seven lessons. Seven downloadable tools. The entire 9-year system I've used to manage 30+ properties and help 230+ people land their first deal."),
    p("A week from now you'll either have run the Mortgage Myth Calculator on your area, made your first landlord call, and started executing the 90-Day Deal Roadmap."),
    p("Or you won't."),
    p("That's the honest fork in the road."),
    p("Jorge had it. He took the playbook, made the calls, signed his first deal in November, and since then he's signed 7 more. It's his full-time job now. He's still scaling."),
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

add("didnt-book-1", "Didn't book", 1, "Ready to map out your first deal?", "48 hours after purchase, if no call booked",
    "GoHighLevel automation “Didn't Book — Book Nudge”, step “Email”", plain([
    "Hi {{contact.first_name}},",
    "You've got everything you need inside The Rent-to-Rent Fast Track to land your first deal. The fastest way to turn it into action is to jump on a call with me.",
    "On the call we'll look at where you're at and map out the exact next steps for your first deal.",
    'Grab a time here:<br/><a href="#">https://capitalpropertytraining.com/confirmation-page-4243</a>',
    "Talk soon,",
    "Ross Cheung",
]))

add("didnt-watch-1", "Got access · didn't watch", 1, "You're in, here's where to start", "24 hours after purchase",
    "GoHighLevel automation “Got Access — Didn't Watch”, step “Email”", plain([
    "Hi {{contact.first_name}},",
    "You've got full access to The Rent-to-Rent Fast Track.",
    "The welcome video is where it clicks. It walks you through how the model actually works, so you can spot your first deal instead of guessing. Most people get through it in one sitting, and at the end it shows you exactly how to book your call with me.",
    "To start, open the Skool invite email we sent you (check spam) and tap Join Now. That opens your course.",
    "Any trouble getting in, just reply to this email and I'll sort it.",
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

if __name__ == "__main__":
    build()
