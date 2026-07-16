# MVP Ops Mail Console Research Monitor

This repository contains a Codex-native monitoring setup for collecting fresh market pain signals about deliverability, reputation, provider filtering, and remediation workflows.

## Structure

- `scripts/run-market-signal-pipeline.codex.md` - canonical pipeline instructions for Codex.
- `scripts/run-market-signal-pipeline.pasha.md` - same pipeline written separately for Pasha.
- `research/config/signal-sources.json` - source list, keyword clusters, and filtering rules.
- `research/config/signal-template.md` - canonical structure for one signal file.
- `research/config/digest-template.md` - canonical structure for daily digests.
- `research/signals/` - one markdown file per normalized signal.
- `research/digests/daily/` - daily digest files for new or updated signals.
- `research/logs/` - per-run execution logs. Tracked in Git.
- `research/state/` - tracked run state and repo-side metadata when the pipeline needs them.
- `automation/codex-hourly-market-monitor.prompt.md` - prompt mirror for the Codex cron automation.

## Codex automation

Use the prompt from `automation/codex-hourly-market-monitor.prompt.md` when creating a recurring Codex automation for this project. The automation should run once every hour, inspect the configured sources, update the markdown database, and then always stage all changed files, commit if there is a diff, and push to `main`.

## Git policy

- All generated and maintained files live in Git.
- The pipeline should use `git add -A`.
- If there are staged changes, commit them and push to branch `main`.
- If there are no file changes, do not create an empty commit.

## Debugging

- Check the newest run log under `research/logs/YYYY-MM-DD/`.
- Read the latest digest under `research/digests/daily/` to confirm what changed.
- If a source is flaky, the automation should log the error and continue with the rest.
- If Git push fails in unattended mode, confirm the remote, branch, and authentication are already configured on the host.

## Recovery

- To rebuild a signal manually, edit or remove only the affected markdown file in `research/signals/` and let the next automation run recreate it.
- To adjust source coverage, edit `research/config/signal-sources.json`.
- If the automation prompt needs to change, update `scripts/run-market-signal-pipeline.codex.md`, `scripts/run-market-signal-pipeline.pasha.md`, and `automation/codex-hourly-market-monitor.prompt.md` together.
