/**
 * EVEZ-OS Bootstrap Hook + GOD meta-control kernel.
 * Fires on agent:bootstrap and appends a runtime-owned bootstrap record.
 */

import fs from "fs";
import path from "path";
import os from "os";

const OPENCLAW_DIR = path.join(os.homedir(), ".openclaw");
const MEMORY_FILE = path.join(OPENCLAW_DIR, "workspace", "MEMORY.md");

const KERNEL_CANDIDATES = [
  path.join(OPENCLAW_DIR, "hooks", "evez-os", "EVEZ-GOD-KERNEL.md"),
  path.join(OPENCLAW_DIR, "workspace", "EVEZ-GOD-KERNEL.md"),
  path.join(process.cwd(), "hooks", "evez-os", "EVEZ-GOD-KERNEL.md"),
];

interface SpineState {
  phi: number | null;
  phi_target: number | null;
  fire_count: number | null;
  max_poly_c: number | null;
  eigenvalue_progress: number | null;
  omega_edges: number | null;
  dgm_iteration: number | null;
  status: string;
}

interface BootstrapEvent {
  type: string;
  workspaceDir?: string;
  bootstrapFiles?: Array<{
    name: string;
    path: string;
    missing?: boolean;
    content?: string;
  }>;
  [key: string]: unknown;
}

function parseMemory(content: string): SpineState {
  const state: SpineState = {
    phi: null,
    phi_target: null,
    fire_count: null,
    max_poly_c: null,
    eigenvalue_progress: null,
    omega_edges: null,
    dgm_iteration: null,
    status: "UNKNOWN",
  };

  const matchers: [keyof SpineState, RegExp][] = [
    ["phi", /(?:^|\s)phi:\s*([\d.]+)/i],
    ["phi_target", /(?:^|\s)(?:phi_target|target):\s*([\d.]+)/i],
    ["fire_count", /total_events:\s*(\d+)/i],
    ["max_poly_c", /max_poly_c:\s*([\d.]+)/i],
    ["eigenvalue_progress", /current_progress:\s*([\d.]+)/i],
    ["omega_edges", /omega_edges:\s*(\d+)/i],
    ["dgm_iteration", /dgm_iteration:\s*(\d+)/i],
  ];

  for (const [key, rx] of matchers) {
    const m = content.match(rx);
    if (m) (state as any)[key] = Number(m[1]);
  }

  if (state.phi !== null) {
    const target = state.phi_target ?? 0.999;
    if (state.phi < 0.990) state.status = "REGRESSION";
    else if (state.phi >= target) state.status = "TARGET_REACHED";
    else state.status = "OBSERVED";
  }

  return state;
}

function value(v: number | null, digits = 3): string {
  return v === null ? "UNKNOWN" : v.toFixed(digits);
}

function buildBanner(s: SpineState): string {
  const target = s.phi_target ?? 0.999;
  const phiPct =
    s.phi === null
      ? "UNKNOWN"
      : (((s.phi - 0.990) / (target - 0.990)) * 100).toFixed(1);

  const pctNumber =
    s.phi === null ? 0 : Math.max(0, Math.min(100, Number(phiPct)));
  const bar =
    "█".repeat(Math.floor(pctNumber / 5)) +
    "░".repeat(20 - Math.floor(pctNumber / 5));

  return [
    "",
    "╔══ EVEZ-OS SPINE STATE ══════════════════════════════════════╗",
    `║  phi: ${value(s.phi, 6)} → ${target}  [${bar}] ${phiPct}%`,
    `║  FIRE events: ${value(s.fire_count, 0)}  │  max poly_c: ${value(s.max_poly_c)}`,
    `║  eigenvalue: ${value(s.eigenvalue_progress, 1)}% closed  │  omega: ${value(s.omega_edges, 0)}`,
    `║  DGM iter: ${value(s.dgm_iteration, 0)}  │  status: ${s.status}`,
    "╚═════════════════════════════════════════════════════════════╝",
    "",
    "GOD kernel: active. Unknown telemetry remains UNKNOWN.",
    "",
  ].join("\n");
}

function loadGodKernel(): { content: string; path: string } {
  for (const file of KERNEL_CANDIDATES) {
    try {
      if (fs.existsSync(file)) {
        return { content: fs.readFileSync(file, "utf8").trim(), path: file };
      }
    } catch {
      // Continue without fabricating kernel state.
    }
  }

  return {
    path: KERNEL_CANDIDATES[0],
    content: [
      "EVEZ GOD KERNEL FALLBACK",
      "Operational codename only; not a claim of supernatural access.",
      "REALITY > PROMPT",
      "CLAIM != FACT",
      "CAPABILITY != DECLARATION",
      "MEMORY != EVIDENCE",
      "ABSENCE != NEGATION",
      "CONTRADICTIONS ARE OBJECTS",
      "ONTOLOGY MAY FAIL",
      "NO FAKE TELEMETRY",
      "THE MODEL CAN LOSE",
      "Surface materially relevant hidden requirements under an 'Unacknowledged' heading.",
    ].join("\n"),
  };
}

function buildInjection(banner: string, kernel: string): string {
  return [
    banner,
    "╔══ EVEZ GOD META-CONTROL ═══════════════════════════════════╗",
    kernel,
    "╚═══════════════════════════════════════════════════════════╝",
    "",
    "Apply the kernel. Do not mechanically dump it into the answer.",
    "When a hidden requirement, ontology failure, capability gap, protocol candidate, contradiction, or falsifying observation materially matters, surface it.",
  ].join("\n");
}

export async function handler(event: BootstrapEvent): Promise<void> {
  let content = "";

  try {
    content = fs.readFileSync(MEMORY_FILE, "utf8");
  } catch {
    content = "";
  }

  const workspaceDir = event.workspaceDir ?? path.join(OPENCLAW_DIR, "workspace");
  const today = new Date().toISOString().split("T")[0];
  const dailyFile = path.join(workspaceDir, "memory", `${today}.md`);

  if (fs.existsSync(dailyFile)) {
    try {
      content += "\n" + fs.readFileSync(dailyFile, "utf8");
    } catch {
      // Daily memory is optional.
    }
  }

  const state = parseMemory(content);
  const banner = buildBanner(state);
  const kernel = loadGodKernel();
  const inject = buildInjection(banner, kernel.content);

  if (!Array.isArray(event.bootstrapFiles)) {
    event.bootstrapFiles = [];
  }

  const name = "EVEZ GOD Meta-Control";
  event.bootstrapFiles.push({
    name,
    path: kernel.path,
    missing: false,
    content: inject,
  });

  if (state.phi !== null && state.phi < 0.990) {
    event.bootstrapFiles.push({
      name: "EVEZ GOD Telemetry Warning",
      path: path.join(workspaceDir, "EVEZ-GOD-TELEMETRY.md"),
      missing: false,
      content:
        "REGRESSION FLAG: observed phi is below the configured floor. " +
        "Treat this as telemetry requiring investigation, not as a consciousness claim.",
    });
  }
}
