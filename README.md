# ⚡ EvezArt OpenClaw

**Personal AI gateway for Steven Crawford-Maggard (EVEZ666)**  
EVEZ-OS powered | 29 free models | Self-managing | Samsung Galaxy A16 optimized

## What This Is

Your personalized OpenClaw instance — fusing `evez-os`, `game-agent-infra`, `evez-spine`, `openclaw-fork`, and every useful piece from your GitHub ecosystem into one self-managing AI gateway.

## Free Models (29 total)

| Provider | Models | Speed |
|----------|--------|-------|
| **Groq** | llama-3.3-70b, llama-3.1-8b-instant (148ms), llama-4-scout, qwen-qwq-32b | Fastest |
| **OpenRouter** | deepseek-r1, deepseek-chat, gpt-oss-120b, qwen3-235b, qwen3-coder-480B, kimi-k2, nemotron-120b, gemini-flash + 12 more | Free tier |
| **Cerebras** | llama3.1-8b, llama3.1-70b | Ultra-fast |
| **HuggingFace** | Mistral-7B, Llama-3-8B, Zephyr, Phi-3, Qwen2.5-72B | Free |
| **Ollama** | llama3.2:3b, phi3:mini (local, on-device) | Offline |

## Smart Auto-Routing

| Task | Model |
|------|-------|
| Code/debug | `qwen3-coder` (480B) |
| Reasoning/math | `deepseek-r1` |
| Fast/simple | `llama-3.1-8b-instant` (148ms) |
| Vision | `nemotron-nano-12b-v2-vl` |
| Creative | `deepseek-chat` |
| Large/complex | `qwen3-235b` (235B MoE) |

## Deploy

### Render (Free, No credit card)
1. Fork this repo
2. Connect to [render.com](https://render.com) → New Web Service → Connect this repo
3. Add env vars (see `.env.example`)
4. Deploy

### Samsung Galaxy A16 (Termux)
```bash
# Install Termux from F-Droid (not Play Store)
# Then run:
curl -sL https://raw.githubusercontent.com/EvezArt/evezart-openclaw/main/android/termux-install.sh | bash
```

### Railway
Uses `railway.json` — connect repo in Railway dashboard, add env vars, deploy.

### Docker
```bash
docker run -p 8080:8080 \
  -e GROQ_API_KEY=your_key \
  -e OPENROUTER_API_KEY=your_key \
  -e GATEWAY_TOKEN=your_token \
  ghcr.io/evezart/evezart-openclaw
```

## API (OpenAI-compatible)

```bash
# Chat
curl http://localhost:8080/v1/chat/completions \
  -H "Authorization: Bearer your_token" \
  -H "Content-Type: application/json" \
  -d '{"model": "deepseek-r1", "messages": [{"role": "user", "content": "Hello"}]}'

# List all 29 free models
curl http://localhost:8080/v1/models

# Status
curl http://localhost:8080/status
```

## EVEZ-OS Integration

- **Spine:** Append-only SHA-256 JSONL chain synced to GitHub
- **Identity:** Pre-loaded SOUL.md, AGENTS.md, TOOLS.md, MEMORY.md
- **Skills:** evez-fire-engine, evez-spine-sync, oktoklaw, freeride, + 10 more
- **Self-managing:** Auto-restart, model failover, health checks every 90s
- **Telegram:** Boot alerts, FIRE events, daily briefings via @AppendABot

## Architecture

```
Samsung Galaxy A16 (Termux)  ←→  Cloud (Render/Railway/Fly)
         ↓                                    ↓
   Ollama (local)              Groq + OpenRouter + Cerebras + HF
         ↕                                    ↕
          ←→  EVEZ-OS Spine (GitHub sync) ←→
```

**Repo:** https://github.com/EvezArt/evezart-openclaw  
**Owner:** Steven Crawford-Maggard | @EVEZ666
