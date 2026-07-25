---
source: "Hacker News"
url: "https://news.ycombinator.com/item?id=23963445"
canonical_id: "2020-07-27-hacker-news-ask-hn-any-improvement-in-gmail-s-treatment-of-small-servers"
comments_supported: "yes"
comments_available_count: 10
comments_parsed_count: 10
parse_status: "complete"
---

## Most Useful Comments Summary
- Deterministic collector preserved the thread comments below for later review.

## Useful Comment Artifacts
- It's been over a year since the Google Is Eating Our Mail (https://www.tablix.org/~avian/blog/archives/2019/04/google_is_eating_our_mail/) post trended on HN. In that thread, a Gmail PM reassured that Google does have an incentive to cooperate with smaller email servers and fix  problems like their mail getting rejected or delivered to the Spam folder when sent to Gmail addresses (https://news.ycombinator.com/item?id=19758386 and https://news.ycombinator.com/item?id=19759411).I'm wondering whether any of you have seen any improvements on this front in the past year. Are there any new introspection tools to diagnose deliverability problems when they happen? New guidelines which verifiably reduce the probability of such problems occurring?As an administrator of a small email server (with SPF/DKIM/DMARC/MTA-STS set up properly and a clean reputation of 5+ years), from my point of view nothing has changed, except perhaps for the worse. Email sent to Gmail users seems to end up in the Spam folder more often than before.
- As an administrator of a small email server, I've never had problems. I even send automated garbage from nagios/munin/etc without SPF or DKIM and it makes it into the inbox on Google.Outlook is where my problems are.
- If your reputation is good enough or if you manually whitelisted nagios/munin/etc. messages, your don't get any problems. Its mainly a problem for new mail server setups (new domain). Bye the way "whitelisting" in Outlook takes some time. But after that, you should not have any problems with Outlook.
- This is what I thought too, but my domain is not that new anymore and things seem to be getting worse. I know all the users personally so I know none of them ever sent any spam so that shouldn't be a problem either.
- Same sad story as always. Gmail & alike surely did "improvements" on email treatment, but it seems that not all infos are publicly available.If you see it the other way around: why should they provide detailed infos for spammers on howto setup their own mailserver.I always wonder why there is not a "Central" Service for each mail provider, like https://postmaster.google.com where you can register your domain and see what is wrong with your mails ... maybe even do "spam protection" by simply adding "mails per second" that you think are appropiate for your service.
- Hmm, thanks for reminding me about Postmaster. The last time I tried using it, I think I ran into the "not enough traffic for your domain, check back later before we allow you to do something useful" brick wall. I'll check it out when I get home, maybe things are better now.> If you see it the other way around: why should they provide detailed infos for spammers on howto setup their own mailserver.I agree that would make no sense. Yet I'm sure the boundary between spammers and use cases like mine is not that ambiguous. I'm very certain that not a single spam email ever got sent out from my mailserver. Surely Google's tech is good enough not to sort that into the same bucket with a typical spammer.
- Just checked and nope, still the same old brick wall, unfortunately.> No data to display at present. Please come back later.
Postmaster Tools requires your domain to satisfy certain conditions before data is visible for this chart. Refer to the Help page for more details.
- I have never had a problem, although I use the ISP's server for sending, and my own computer for receiving; when setting up Exim you can select the "smart host" option which does this.
- I'm reluctant to switch to a third party for sending because I like to do it myself, but perhaps I'll have to do this.
- The sad part is you can use any mainstream email sending service like sendgrid and it works no problem. You can even have a completely phony "From:" header and it will land in the inbox [0]. And BTW gmail isn't even the worst, I could still easily make it into spam from my own server. With outlook/hotmail I couldn't even make it that far.I wish people who praise Email as an example of decentralization working actually went through that exercise.[0] yes it will show "via sendgrid.net" so perhaps by design the domain in "From" isn't checked, but still...
