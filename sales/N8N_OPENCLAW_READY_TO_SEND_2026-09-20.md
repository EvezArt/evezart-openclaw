# READY-TO-SEND TRIAL PACKET — HUMAN APPROVAL REQUIRED

## Target
n8n Community: "OpenClaw + VPS person — paid trial task, ongoing work"
Verified active 2026-09-20. Remote, any timezone.

## Draft reply

I work on OpenClaw-style runtime/deployment infrastructure and have an EVEZ deployment surface covering OpenClaw, Termux/Android, workflow orchestration, and evidence/provenance.

Relevant artifacts:
- https://github.com/EvezArt/evez-openclaw-deploy
- https://github.com/EvezArt/evez-openclaw-apk
- https://github.com/EvezArt/evezart-openclaw

For a bounded paid trial, I would keep the environment isolated and document the exact state before and after each change. The target hardening pattern I would test includes a dedicated non-sudo user, SSH key-only access, UFW/fail2ban, loopback binding where appropriate, 0600 secret permissions, service supervision, monitoring, and a concise runbook.

I would not use production credentials on a trial VPS. I would record the acceptance evidence and any deviations from the requested baseline.

I am interested in ongoing work if the paid trial demonstrates a good technical fit.

## Before sending
Confirm the exact trial scope, payment, access method, acceptance criteria, and recording requirement.
