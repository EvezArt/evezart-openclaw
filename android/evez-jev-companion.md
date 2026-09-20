# Galaxy A16 companion plan

The Galaxy A16 is an edge/control device, not the primary model server.

## Offline behavior

- write commands, notes, and sensor summaries to a local queue;
- attach a monotonic event id and timestamp to every queued item;
- retry sync only when connectivity is available;
- deduplicate on the VPS by event id;
- keep the local queue encrypted by Android storage protections;
- show stale-data status clearly in the UI.

## Termux surface

The companion may use Termux and Termux:API for local scripts and selected device APIs. It must not store parent gateway secrets in source files. Use a short-lived, scoped enrollment credential and revoke it when the device is removed.

## Private networking

Use Tailscale/Serve or another authenticated private path when available. Do not use Funnel or an unauthenticated public port for the gateway. Network loss must degrade to queueing, not disable authorization checks.

## First implementation slice

1. status screen;
2. local command queue;
3. authenticated sync endpoint;
4. gateway health display;
5. manual retry and export;
6. sensor adapter behind an explicit permission switch.
