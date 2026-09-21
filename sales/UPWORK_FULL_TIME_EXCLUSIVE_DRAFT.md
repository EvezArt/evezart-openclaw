# Upwork application draft — Full-Time AI Automation Developer

Status: DRAFT ONLY. Not submitted.

Target: Full-Time AI Automation Developer — n8n, AI Agents & Full-Stack
Observed listing: $2,500-$4,000/month target, 40 hrs/week, long-term, exclusive, paid technical trial. The listing asks for the proposal to begin with "FULL-TIME EXCLUSIVE — AI DEVELOPER", two relevant projects, a 3–5 minute walkthrough, GitHub/code sample, separate tool experience, compensation/location/timezone/notice/start date, a failure example, trial confirmation, and an exclusivity statement.

## Proposed application

FULL-TIME EXCLUSIVE — AI DEVELOPER

I build AI automation and agent systems with a strong emphasis on the parts that make them operable after the demo: API integrations, workflow state, retries, failure handling, logging, deployment, documentation, and human approval boundaries.

Two relevant projects I personally built:

1. EVEZ-OS / OpenClaw runtime surface
https://github.com/EvezArt/evezart-openclaw
I built and organized an OpenClaw/EVEZ runtime surface around agent orchestration, an OpenAI-compatible gateway, VCL visualization, deployment surfaces, and an Android client. The repository is public and inspectable. Current production status of individual deployments is distinguished from repository artifacts rather than assumed.

2. EvezArt OpenClaw Android client
https://github.com/EvezArt/evez-openclaw-android
I built the Android client surface that can load an OpenClaw web UI, including local/remote gateway configuration and a Termux-oriented build path. It is a concrete example of connecting an agent/runtime system to a mobile operational surface.

3–5 minute walkthrough:
I will demonstrate one bounded workflow end-to-end, showing the trigger, validation, agent/workflow execution, logging/evidence, failure handling, and resulting artifact. I will only present behavior verified during the recording.

Tool experience:
- n8n: personal project / workflow-engineering work; event-driven automation, APIs, integrations, error handling and operational patterns.
- OpenClaw: personal project; installation/configuration, runtime integration and EVEZ/OpenClaw surfaces.
- Hermes: no independently verified production experience to claim; willing to learn the client's specific deployment.
- Claude Code: personal development workflow where available.
- Codex: personal development workflow.
- Anthropic API: integration work where used; exact current deployments should be verified before claiming production status.
- OpenAI API: integration work and OpenAI-compatible gateway surfaces.
- xAI/Grok API: no independently verified production deployment to claim.
- Python: personal/backend automation and tooling.
- JavaScript/TypeScript: web/backend automation and application work.
- PostgreSQL/database systems: project work and automation architecture.
- GitHub: extensive repository, branch, commit, issue and deployment workflow use.
- Deployment: Linux, Docker/containerized systems, hosted application surfaces, environment configuration and operational documentation.

System failure example:
A useful failure pattern I have worked around is treating automation state as implicit. The fix is to make state explicit: validate inputs, assign stable identifiers, make writes idempotent, capture execution evidence, handle retries/timeouts, and route ambiguous or consequential actions to human approval rather than guessing. That same pattern is what I would apply to your production workflows.

Compensation:
Proposed target: $4,000 USD/month for the stated 40-hour/week full-time engagement, subject to the agreed paid technical trial and platform fees.

Location/time zone:
United States; Pacific Time (UTC-7 on the current date).

Notice period:
I would transition into the exclusive arrangement after the paid technical trial and an agreed start date. I am not representing an existing employment notice period that has not been verified.

Earliest exclusive start:
Immediately after the paid trial and mutually agreed transition date, subject to confirming the required 40-hour schedule.

Working hours:
I can structure the 40-hour week around the required overlap with US Eastern Time. The exact daily schedule should be confirmed before the exclusive start date.

Paid technical trial:
Confirmed. I am willing to complete a scoped paid technical trial with scope, acceptance criteria, access boundaries, and payment agreed beforehand through Upwork.

Exclusivity:
I understand this is a long-term, full-time, exclusive engagement. If selected, I will make this my only employer/client, end other paid work commitments before my agreed exclusive start date, commit 40 hours per week, and personally perform the work.

My working principle is simple: ship the smallest reliable system that solves the business problem, instrument it so failures are visible, and leave enough documentation that another engineer can understand what happened without archaeology.

