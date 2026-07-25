---
source: "Server Fault"
url: "https://serverfault.com/questions/1195797/why-does-email-sent-with-php-mail-land-in-spam-while-authenticated-smtp-mail-f"
canonical_id: "2025-11-06-server-fault-why-does-email-sent-with-php-mail-land-in-spam-while-authent"
comments_supported: "yes"
comments_available_count: 3
comments_parsed_count: 3
parse_status: "complete"
---

## Most Useful Comments Summary
- Deterministic collector preserved the thread comments below for later review.

## Useful Comment Artifacts
- As already commented your question needs some more details to conclusively answer but When you don’t adjust the php.ini sendmail_path with postfix sendmail options like the  -r and/or -f options,  the envelope sender will typically be the-php-or-www-user@fqdn-hostname rather than user@domain and that probably fails to match to your DKIM setup. Check your logs and the raw headers.
- Please locate your PHP INI file and post the [mail function] section. There may be several different config files for PHP depending on whether you are running it from the command line, as an Apache module, or as an FPM service.
- Please show your Postfix configuration (postconf -n).
