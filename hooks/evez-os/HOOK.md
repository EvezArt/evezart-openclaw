---
name: evez-os
description: "EVEZ-OS spine state plus GOD meta-control kernel"
metadata:
  { "openclaw": { "events": ["agent:bootstrap", "command:new", "command:reset"] } }
---

# EVEZ-OS + GOD bootstrap hook

Runs on agent bootstrap and injects two runtime-owned context blocks:

1. Observed EVEZ-OS spine telemetry when it is actually present in memory.
2. The EVEZ GOD meta-control kernel, which forces the model to inspect latent requirements, capability gaps, ontology failures, contradictions, protocol candidates, and falsifying evidence.

Missing telemetry stays UNKNOWN. The hook never invents measurements.

The GOD kernel is an operational control layer. Its name does not claim supernatural access, omniscience, or consciousness.

The handler mutates event.bootstrapFiles, which is the supported agent:bootstrap delivery contract.

Enable:

openclaw hooks enable evez-os

After editing an existing hook, restart the Gateway and verify the hook with:

openclaw hooks info evez-os
openclaw hooks list --eligible

The hook must be installed on the Gateway host, because bootstrap hooks execute there.