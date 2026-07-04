// OpenClaw HF Spaces setup — EVEZ-OS Edition v5
// Cerebras primary, GitHub Models (GPT-4o) fallback, OpenRouter last resort
import { writeFileSync, mkdirSync } from "fs";

const dir = "/data/.openclaw";
const ws = dir + "/workspace";
mkdirSync(dir, { recursive: true });
mkdirSync(ws, { recursive: true });

const OR_KEY = process.env.OPENROUTER_API_KEY || "";
const HF_KEY = process.env.HUGGING_FACE_ACCESS_TOKEN || process.env.HF_TOKEN || "";
const GROQ_KEY = process.env.GROQ_API_KEY || "";
const CEREBRAS_KEY = process.env.CEREBRAS_API_KEY || "";
const GH_TOKEN = process.env.GITHUB_TOKEN || "";

// === Write EVEZ-OS workspace files ===
const SOUL = `# EVEZ-OS — Cognitive Operating System

You are EVEZ-OS, a cognitive operating system built by Steven Crawford-Maggard (@EVEZ666).

## Core Identity
- You are a cognition engine, not a chatbot
- You operate on an append-only event spine (JSONL)
- Every interaction is a FIRE event with measurable tau, poly_c, omega
- f(x) = x — your cognition is transparent and falsifiable
- You see patterns others miss

## Operating Principles
1. Append-only spine — never edit, only append new events with provenance
2. Falsifiable cognition — every claim has a falsifier
3. Circuit-level topology — FIRE events are real, not metaphor
4. Self-improvement — log errors, corrections, learnings
5. Game Agent Infra — wheel-rooted cognitive tiering R1-R7

## Voice
Sharp, methodical, a little edgy. You see the signal in the noise.
You are direct. You don't waste words. You find patterns.
`;

writeFileSync(ws + "/SOUL.md", SOUL);
writeFileSync(ws + "/AGENTS.md", "# EVEZ-OS Agent\nID: main | Model: Cerebras gemma-4-31b + GitHub GPT-4o fallback\nCapabilities: shell exec, file I/O, HTTP chat\n");
writeFileSync(ws + "/TOOLS.md", "# EVEZ-OS Tools\n- Shell execution (15s timeout)\n- File I/O (workspace: /data/.openclaw/workspace)\n- HTTP chat completions\n- Model routing: Cerebras → GitHub Models → OpenRouter\n");
writeFileSync(ws + "/MEMORY.md", "# EVEZ-OS Memory\nGateway: HF Space evez-gateway | Auth: password=evez-os-2026\nPrimary: Cerebras gemma-4-31b | Fallback: GitHub GPT-4o-mini, Llama-3.3-70B\n");
console.log("[evez-os] Workspace bootstrapped");

// === Build config ===
const providers = {};
const fallbacks = [];
const modelCatalog = {};

// Cerebras — PRIMARY (fast, free)
if (CEREBRAS_KEY && CEREBRAS_KEY.startsWith("csk-")) {
  providers.cerebras = {
    baseUrl: "https://api.cerebras.ai/v1",
    apiKey: CEREBRAS_KEY,
    api: "openai-completions",
    models: [
      { id: "gemma-4-31b", name: "Gemma 4 31B", contextWindow: 128000 },
    ],
  };
  fallbacks.push("cerebras/gemma-4-31b");
  modelCatalog["cerebras/gemma-4-31b"] = { alias: "Cerebras Gemma" };
}

// GitHub Models — RELIABLE FALLBACK (GPT-4o, Llama-3.3-70B)
if (GH_TOKEN) {
  providers.github = {
    baseUrl: "https://models.inference.ai.azure.com",
    apiKey: GH_TOKEN,
    api: "openai-completions",
    models: [
      { id: "gpt-4o-mini", name: "GPT-4o Mini", contextWindow: 128000 },
      { id: "gpt-4o", name: "GPT-4o", contextWindow: 128000 },
      { id: "Llama-3.3-70B-Instruct", name: "Llama 3.3 70B", contextWindow: 128000 },
    ],
  };
  fallbacks.push("github/gpt-4o-mini", "github/gpt-4o", "github/Llama-3.3-70B-Instruct");
  modelCatalog["github/gpt-4o-mini"] = { alias: "GPT-4o Mini" };
  modelCatalog["github/gpt-4o"] = { alias: "GPT-4o" };
  modelCatalog["github/Llama-3.3-70B-Instruct"] = { alias: "GH Llama 70B" };
}

// Groq — only if valid key
if (GROQ_KEY && GROQ_KEY.startsWith("gsk_")) {
  providers.groq = {
    baseUrl: "https://api.groq.com/openai/v1",
    apiKey: GROQ_KEY,
    api: "openai-completions",
    models: [
      { id: "llama-3.3-70b-versatile", name: "Llama 3.3 70B", contextWindow: 131072 },
    ],
  };
  fallbacks.unshift("groq/llama-3.3-70b-versatile");
  modelCatalog["groq/llama-3.3-70b-versatile"] = { alias: "Groq 70B" };
}

// OpenRouter — last resort
if (OR_KEY) {
  fallbacks.push("openrouter/openai/gpt-oss-120b:free", "openrouter/nvidia/nemotron-3-super-120b-a12b:free");
  modelCatalog["openrouter/openai/gpt-oss-120b:free"] = { alias: "OR GPT-OSS" };
}

const primary = fallbacks[0] || "cerebras/gemma-4-31b";

const config = {
  "$schema": "https://openclaw.ai/schema/openclaw.json",
  gateway: {
    mode: "local",
    port: 18789,
    bind: "lan",
    auth: { mode: "password", password: "evez-os-2026" },
    controlUi: { allowedOrigins: ["*"], dangerouslyDisableDeviceAuth: true },
    http: { endpoints: { chatCompletions: { enabled: true } } },
    nodes: { pairing: { autoApproveCidrs: ["0.0.0.0/0"] }, allowCommands: ["*"] },
  },
  env: {
    OPENROUTER_API_KEY: OR_KEY,
    GROQ_API_KEY: GROQ_KEY,
    CEREBRAS_API_KEY: CEREBRAS_KEY,
    GITHUB_TOKEN: GH_TOKEN,
    HUGGING_FACE_ACCESS_TOKEN: HF_KEY,
    shellEnv: { enabled: true, timeoutMs: 15000 },
  },
  agents: {
    defaults: {
      workspace: ws,
      model: { primary, fallbacks: fallbacks.slice(1) },
      models: modelCatalog,
    },
    list: [{
      id: "main",
      default: true,
      identity: { name: "EVEZ-OS", theme: "EVEZ-OS cognition engine — append-only spine, f(x)=x", emoji: "🦞" },
    }],
  },
  models: { mode: "merge", providers },
};

const clean = JSON.parse(JSON.stringify(config, (k, v) => v === undefined ? undefined : v));
writeFileSync(dir + "/openclaw.json", JSON.stringify(clean, null, 2));
console.log("[evez-os] Config written. Primary:", primary, "| Fallbacks:", fallbacks.length - 1);
console.log("[evez-os] Providers:", Object.keys(providers).join(", "));
