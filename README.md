---
title: EVEZ-OS KAX VCL Runtime
emoji: ⚡
colorFrom: green
colorTo: black
sdk: docker
app_port: 7860
pinned: true
license: mit
---

# EVEZ-OS KAX VCL Runtime

Generative VCL runtime and OpenAI-compatible gateway surface.

## Security

Gateway credentials are supplied through deployment secrets/environment configuration and are intentionally not stored in this repository. Rotate any credential that was previously committed to public source control.

## Endpoints

- `GET /` — VCL visualizer
- `GET /health` — system state
- `GET /api/substrate` — substrate data
- `WS /ws/vcl` — VCL stream
- `POST /v1/chat/completions` — OpenAI-compatible interface
- `GET /v1/models` — available models

## OpenClaw Surface

- Main deploy repo: https://github.com/EvezArt/evez-openclaw-deploy
- Android/A16 app: https://github.com/EvezArt/evez-openclaw-apk
- Local dashboard: `http://localhost:18789`
- Termux bootstrap: `scripts/a16-termux-bootstrap.sh` in the deploy repo

The intended architecture is a shared OpenClaw gateway surface connecting EVEZ Station, VCL, NEXUS, ClawBreak, Telegram, Slack, PWA, and Android clients. Verify each deployment before describing it as live.
