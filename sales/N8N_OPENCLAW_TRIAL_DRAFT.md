# n8n Community application draft — OpenClaw + VPS paid trial

Status: DRAFT ONLY. Not posted.

Target: [HIRING] OpenClaw + VPS person — paid trial task, ongoing work
Observed requirements: fresh Hetzner Ubuntu 24.04 VPS; pinned OpenClaw; dedicated non-sudo user; systemd; SSH key-only; UFW; fail2ban; loopback binding; monitoring; secrets in 0600 env files; runbook; screen recording; then possible ongoing agent boxes, n8n production workflows and on-call fixes.

## Reply draft

Hi James,

1. Telegram photo -> job record

I would have the Telegram event capture the file_id, sender, timestamp and any job reference supplied in the message. n8n would validate that reference against the active production records before writing anything, then download the image into durable job-keyed storage and write the resulting file reference plus Telegram message metadata back to the matching job. I would make the write idempotent so retries cannot create duplicate attachments. If the job match is missing or ambiguous, the workflow should stop and route the item to a review queue rather than guessing.

2. Most relevant build

EVEZ-OS KAX VCL / OpenClaw runtime:
https://github.com/EvezArt/evezart-openclaw

The repository is a public OpenClaw/EVEZ runtime surface. I can demonstrate the relevant runtime/deployment structure and distinguish repository evidence from anything that needs to be verified live.

3. Trial quote and ongoing rate

Trial: US$400 fixed for the stated single-VPS scope, including the agreed OpenClaw installation/configuration, hardening, monitoring configuration, runbook and screen recording.

Ongoing: US$60/hour, or fixed milestones when the scope is sufficiently defined.

4. Timezone and urgent work

United States Pacific Time (UTC-7 on the current date). For urgent work, I prefer an explicit response window agreed as part of the engagement rather than promising an unbounded on-call commitment before the schedule is defined.

I like the way you are treating the screen recording and runbook as part of the actual deliverable rather than as an afterthought. My approach is to leave every important decision and operational step reproducible.

I would start on the throwaway VPS only, keep production credentials out of the trial environment, and document the handoff.

Best,
Steven / EVEZ
