# Comment Source Registry

Use this file to remember whether already parsed items are worth revisiting for comments.

## Fields to track per item

- source
- url
- comments_supported: yes|no|unknown
- comments_last_checked_at
- comments_recheck_policy: periodic|skip
- note

## Rules

- Set `comments_recheck_policy: periodic` only when comments can actually be fetched.
- Set `comments_recheck_policy: skip` when comments are disabled, unavailable, or not fetchable.
- Do not re-fetch a parsed article only to look for comments after it has been marked `skip`.
- If a useful new comment is found later, update the existing canonical signal where possible instead of duplicating the article.
