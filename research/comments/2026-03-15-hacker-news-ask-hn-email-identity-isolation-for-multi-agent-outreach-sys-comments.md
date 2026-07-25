---
source: "Hacker News"
url: "https://news.ycombinator.com/item?id=47386460"
canonical_id: "2026-03-15-hacker-news-ask-hn-email-identity-isolation-for-multi-agent-outreach-sys"
comments_supported: "yes"
comments_available_count: 1
comments_parsed_count: 1
parse_status: "complete"
---

## Most Useful Comments Summary
- Deterministic collector preserved the thread comments below for later review.

## Useful Comment Artifacts
- Been building an AI agent pipeline for outbound email and ran into an infrastructure problem that I haven't seen discussed much.When you run multiple agents doing outreach in parallel, the default setup most people land on is having all agents share one email domain and sending identity. This breaks in a few ways at scale:1. Reputation isolation: if one agent gets flagged for aggressive sending or trips spam filters, the entire domain reputation degrades. Every other agent's deliverability takes the hit even if they're running fine.2. Reply attribution: all inbound replies land in one inbox with no clean way to route them back to the specific agent that initiated the conversation. Makes conversion tracking nearly impossible.3. Per-agent A/B testing: impossible to test different messaging approaches at the agent level when they all share an identity.The pattern that seems right is giving each agent its own dedicated sending address so reputation is isolated per agent and replies route back correctly. But the tooling to do this cleanly - especially the inbound routing piece - doesn't seem to exist in a plug-and-play way for agent workflows.Curious how others have solved this. Are you managing separate identities manually, using some existing tool I've missed, or just accepting the shared domain limitations for now?
