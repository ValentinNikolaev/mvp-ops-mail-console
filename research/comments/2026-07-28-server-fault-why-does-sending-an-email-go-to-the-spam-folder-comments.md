---
source: "Server Fault"
url: "https://serverfault.com/questions/1199571/why-does-sending-an-email-go-to-the-spam-folder"
canonical_id: "2026-07-28-server-fault-why-does-sending-an-email-go-to-the-spam-folder"
comments_supported: "yes"
comments_available_count: 5
comments_parsed_count: 5
parse_status: "complete"
---

## Most Useful Comments Summary
- Deterministic collector preserved the thread comments below for later review.

## Useful Comment Artifacts
- This question is similar to: How to send emails and avoid them being classified as spam?. If you believe it’s different, please edit the question, make it clear how it’s different and/or how the answers on that question are not helpful for your problem.
- The MX record is not blacklisted on mxtoolbox. The SPF on mxtoolbox says the domain is ok  (PrefixDesc SoftFail) while spf-record.com says it is not (one record found - spf check failed).
- Right now I would suggest that you check a few things by yourself. Otherwise you would be revealing probably more than you want to the public. 2 sites I would recommend.  1) mxtoolbox.com Let&#39;s you check your domain&#39;s MX record and if it is blacklisted  2) spf-record.com Checks your SPF record and some other stuff as well  I fear there is a mistake in your domain settings, like MX record or spf record. Those sites should help you find it.
- It&#39;s is outsourced to Networksolutions. I had another domain with them and never had this issue but that domain is no loger in use. Yes, it offers dns servers.
- Hello jmstanley. Your post doesn&#39;t contain many information. A few things you should clarify. What is your email server? Do you have your own Microsoft Exchange server? Do you use Exchange Online? Or something different? When you say &quot;This is a new domain&quot;, does  that mean a new domain on the mail server? Or is this a start of a new company? Also, where did you register your domain? Does that platform offer DNS services for your domain?
