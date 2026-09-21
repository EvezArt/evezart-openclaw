# EVEZ / OpenClaw client demo package

## Purpose

A buyer-facing, evidence-first demonstration of workflow engineering, agent orchestration, deployment discipline, and provenance.

This package deliberately separates:
- OBSERVED: code/repository artifacts that can be inspected.
- VERIFIED-LIVE: runtime behavior demonstrated during the current demo.
- INFERRED: architecture or intended behavior not currently exercised.
- UNKNOWN: capabilities that require a fresh environment check.

## 3-5 minute speedrun

0:00-0:20 — Identity and scope
"I build AI automation and agent systems with explicit state, integrations, failure handling, and evidence. I will show only what I can verify."

0:20-1:00 — Repository surface
Open the EVEZ OpenClaw repository and show the runtime README, deployment surfaces, and Android client. Explain the shared-gateway architecture without claiming every surface is currently deployed.

1:00-1:50 — Workflow/evidence model
Show event-spine/watchdog concepts and explain the production pattern:
trigger -> validate -> execute -> observe -> retry/fail -> append evidence -> human approval where needed.

1:50-2:40 — Agent execution
Run one bounded workflow. Capture inputs, outputs, timestamps, errors, and resulting artifact. No fabricated metrics.

2:40-3:20 — Reliability
Show a deliberate failure or simulated failure path, then show retry/rollback/manual-approval behavior. The buyer should see that the system is designed to keep working when an API misbehaves.

3:20-4:10 — Deployment
Show the deployment target and health endpoint, or clearly label it as a local/test environment. Explain secrets, environment configuration, logs, and reproducibility.

4:10-4:45 — Commercial handoff
Offer a paid first milestone:
1. audit one workflow;
2. implement one production workflow;
3. add logging/retries/deduplication;
4. document it;
5. deliver a reproducible handoff.

## Proposal language

I build AI automation systems around the boring parts that determine whether they survive production: explicit state, API integration, retries, error handling, logging, deployment, and reproducible handoffs.

My EVEZ/OpenClaw work gives me a broad working surface across agent orchestration, workflow automation, dashboards, deployment, and evidence/provenance. For an initial paid milestone, I would keep the scope narrow: take one business workflow from trigger to verified output, add failure handling and observability, and leave you with documentation and a reproducible test path.

I am comfortable working with n8n, APIs/webhooks, Python/JavaScript, GitHub, databases, containers, and AI model integrations. I prefer measurable acceptance criteria over vague "AI agent" promises.

For the first milestone I would propose:
- map the existing workflow;
- identify failure and duplicate paths;
- implement the smallest production-ready automation;
- add logging/retry/approval boundaries;
- test representative success and failure cases;
- deliver the workflow plus concise operating documentation.

I can then continue with additional workflows or ongoing maintenance if the first milestone proves useful.

## Evidence policy

Do not claim:
- revenue not independently verified;
- uptime not currently measured;
- deployments not currently reachable;
- government endorsement/appointment;
- hardware attestation as proof of physical identity;
- autonomous operation where human approval is required.

Link directly to inspectable repositories and current demos.
