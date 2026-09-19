/**
 * EVEZ-OS Bootstrap Hook + GOD meta-control kernel.
 * Fires on agent:bootstrap and injects verified spine state plus
 * the latent-response rules that force the model to expose its own blind spots.
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

  const pctNumber = s.phi === null ? 0 : Math.max(0, Math.min(100, Number(phiPct)));
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

function loadGodKernel(): string {
  for (const file of KERNEL_CANDIDATES) {
    try {
      if (fs.existsSync(file)) {
        return fs.readFileSync(file, "utf8").trim();
      }
    } catch {
      // Continue to the next candidate without fabricating kernel state.
    }
  }

  return [
    "EVEZ GOD KERNEL FALLBACK",
    "This fallback preserves the critical laws when the full kernel file is unavailable.",
    "REALITY > PROMPT",
    "CLAIM != FACT",
    "CAPABILITY != DECLARATION",
    "MEMORY != EVIDENCE",
    "ABSENCE != NEGATION",
    "CONTRADICTIONS ARE OBJECTS",
    "ONTOLOGY MAY FAIL",
    "NO FAKE TELEMETRY",
    "THE MODEL CAN LOSE",
    "Surface material hidden requirements under an 'Unacknowledged' heading when they materially change the answer.",
  ].join("\n");
}

function buildInjection(banner: string, kernel: string): string {
  return [
    banner,
    "╔══ EVEZ GOD META-CONTROL ═══════════════════════════════════╗",
    kernel,
    "╚═══════════════════════════════════════════════════════════╝",
    "",
    "Do not mechanically dump the kernel into the answer. Apply it.",
    "When a hidden requirement, ontology failure, capability gap, protocol candidate, contradiction, or falsifying observation materially matters, surface it.",
  ].join("\n");
}

export async function handler(event: { type: string }) {
  let content = "";

  try {
    content = fs.readFileSync(MEMORY_FILE, "utf8");
  } catch {
    content = "";
  }

  const today = new Date().toISOString().split("T")[0];
  const dailyFile = path.join(
    OPENCLAW_DIR,
    "workspace",
    "memory",
    `${today}.md`,
  );

  if (fs.existsSync(dailyFile)) {
    try {
      content += "\n" + fs.readFileSync(dailyFile, "utf8");
    } catch {
      // Daily memory is optional; absence is not a claim about its contents.
    }
  }

  const state = parseMemory(content);
  const banner = buildBanner(state);
  const kernel = loadGodKernel();
  const inject = buildInjection(banner, kernel);

  if (state.phi !== null && state.phi < 0.990) {
    return {
      inject:
        inject +
        "\n\nREGRESSION FLAG: observed phi is below the configured floor. " +
        "Treat this as telemetry requiring investigation, not as a consciousness claim.\n",
    };
  }

  return { inject };
}
