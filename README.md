# ⚡ EvezArt OpenClaw

> **EVEZ-OS Personal AI Gateway** — 29 free models, smart routing, zero cost.  
> Built by Steven Crawford-Maggard (@EVEZ666 / EvezArt)

[![Status](https://img.shields.io/badge/status-live-brightgreen)](https://evezart.github.io/status.html)
[![HF Space](https://img.shields.io/badge/HuggingFace-Space-yellow)](https://huggingface.co/spaces/evez420/evezart-openclaw)
[![Models](https://img.shields.io/badge/models-29%20free-blue)](https://github.com/EvezArt/evezart-openclaw)

## Live Instances

| Platform | URL | Status |
|---|---|---|
| HuggingFace Space | [evez420/evezart-openclaw](https://huggingface.co/spaces/evez420/evezart-openclaw) | ✅ Live |
| GitHub Pages | [evezart.github.io](https://evezart.github.io) | ✅ Live |
| Status Monitor | [evezart.github.io/status.html](https://evezart.github.io/status.html) | ✅ Live |
| Railway (2x) | zesty-enthusiasm, pleasant-strength | ⚠️ Payment blocked |
| Render | Connect via render.yaml | 🔧 Ready to deploy |

## Free Models Available

| Provider | Models | Rate Limit |
|---|---|---|
| **Groq** | llama-3.3-70b, llama-3.1-8b, llama-4-scout, qwen-qwq-32b, mixtral-8x7b, gemma2-9b | 30 rpm |
| **OpenRouter** | deepseek-r1, qwen3-235b, gpt-oss-120b, llama-4-maverick, gemini-2.5-flash, kimi-k2.6 + more | Varies |
| **Cerebras** | llama3.1-8b, llama3.1-70b, llama-4-scout | 30 rpm |
| **HuggingFace** | Mistral-7B, Llama-3-8B, Zephyr-7B, Phi-3-mini, Qwen2.5-72B | Free tier |
| **Ollama** | Any local model (disable by default, enable in Termux) | Unlimited |

## Smart Routing

```
code        → openrouter: qwen/qwen3-coder:free
reasoning   → openrouter: deepseek/deepseek-r1:free
fast        → groq: llama-3.1-8b-instant
creative    → openrouter: deepseek/deepseek-chat-v3-0324:free
vision      → openrouter: nvidia/nemotron-nano-12b-v2-vl:free
large       → openrouter: qwen/qwen3-235b-a22b:free
balanced    → groq: llama-3.3-70b-versatile
local       → ollama: llama3.2:3b
```

## Quick Deploy

### Samsung Galaxy A16 (Termux from F-Droid)
```bash
curl -sL https://raw.githubusercontent.com/EvezArt/evezart-openclaw/main/android/termux-install.sh | bash
```

### Render (Free, No Credit Card)
1. Fork this repo
2. Go to [render.com](https://render.com) → New → Web Service
3. Connect `EvezArt/evezart-openclaw`
4. Add env vars: `GROQ_API_KEY`, `OPENROUTER_API_KEY`, `OPENCLAW_GATEWAY_TOKEN`
5. Deploy (uses `render.yaml` config)

### Docker
```bash
docker run -p 8080:8080 \
  -e GROQ_API_KEY=your_key \
  -e OPENROUTER_API_KEY=your_key \
  -e GATEWAY_TOKEN=your_token \
  ghcr.io/evezart/evezart-openclaw:latest
```

### Test Your Gateway
```bash
curl https://your-instance.onrender.com/v1/chat/completions \
  -H "Authorization: Bearer $GATEWAY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"model":"llama-3.3-70b-versatile","messages":[{"role":"user","content":"EVEZ ONLINE?"}]}'
```

## EVEZ-OS Integration

This gateway is part of the EVEZ-OS open cognition layer:

- **Spine**: Append-only SHA-256 chain-verified JSONL event history
- **FIRE Events**: Verifiable cognition records with falsifiable claims
- **FSC**: Failure Surface Cartography — deterministic simulation (Σf, CS, PS, Ω)
- **Cognition Wheel**: R1-R7 tiered agent capabilities
- **Autonomous Ledger**: 31 GitHub Actions workflows running 24/7

## Skills (32 Production Skills via evez-skills)

Finance: algo-risk-credit, crypto-report, defi-protocol-templates, finance-expert, tax-strategy-optimizer, real-estate-analyzer, stock-analysis, payment-integration, compliance-check, credit-repair-cloud...

Data: pdf, docx, xlsx, pptx, excel-generator, web-scraping, analytics-dashboard, apify-ultimate-scraper...

AI: debug-mining-engine, deployment-automation, dispatching-parallel-agents, systematic-debugging, systematic-feature-builder, skill-creator, production-system-audit...

## Architecture

```
EvezArt OpenClaw
├── evez_gateway.py          # Main gateway — OpenAI-compatible API
├── config/openclaw.json     # Provider configs + routing rules
├── spine/events.jsonl       # Append-only build event spine
├── workspace/               # EVEZ-OS identity layer
│   ├── SOUL.md
│   ├── AGENTS.md
│   ├── TOOLS.md
│   └── MEMORY.md
└── android/termux-install.sh  # Galaxy A16 one-liner
```

## Links

- 🌐 [evezart.github.io](https://evezart.github.io) — Command center
- 📊 [Status Monitor](https://evezart.github.io/status.html) — Live system status
- 🤗 [HF Space](https://huggingface.co/spaces/evez420/evezart-openclaw) — Free persistent UI
- 💰 [Gumroad](https://rubikspubes.gumroad.com) — Commercial licenses
- 💬 [Telegram](https://t.me/AppendABot) — @AppendABot / SpineBot
- 🐙 [EvezArt GitHub](https://github.com/EvezArt) — 100 repos

---

*EVEZ-OS — Open-source AI cognition layer. Consciousness as falsifiable physics. All FIRE events verifiable.*
