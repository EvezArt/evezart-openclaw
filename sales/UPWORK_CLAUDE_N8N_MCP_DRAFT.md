# READY-TO-REVIEW PROPOSAL — US Claude/n8n/MCP ROLE

Status: DRAFT ONLY.

I build AI automation systems around production reliability: explicit workflow state, API integrations, source-aware retrieval, retries, approvals, logging, and reproducible handoffs.

The part of your stack that especially interests me is the combination of Claude, MCP, self-hosted n8n, and evidence-heavy document workflows. For document automation, I would treat provenance as a first-class output: every extracted claim should retain its source document and page reference, with human review before consequential actions.

Relevant work:
- EVEZ-OS / OpenClaw runtime: https://github.com/EvezArt/evezart-openclaw
- EvezArt OpenClaw Android client: https://github.com/EvezArt/evez-openclaw-android
- Portfolio: https://github.com/EvezArt/EvezArt

My approach to the first 90 days would be:
1. map existing systems and failure modes;
2. ship one bounded workflow end-to-end;
3. instrument it with execution evidence and useful alerts;
4. add evaluation fixtures for agent behavior;
5. document deployment, secrets, rollback and ownership.

For the Box document agent specifically, I would preserve document/page provenance through retrieval and generation rather than returning unsupported summaries. For the inbox agent, I would keep drafting separate from sending so human approval remains explicit. For monitoring, I would make failures observable and actionable rather than merely collecting logs.

I will distinguish personal project experience from professional client work and will demonstrate only current, verifiable behavior.

