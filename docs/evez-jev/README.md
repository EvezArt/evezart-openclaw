# EvezJev integration

EvezJev is the structured-decision layer for the EvezArt OpenClaw stack.

## Responsibilities

- classify and route work to local, hosted, or human-review paths;
- score AI-product and crypto-research opportunities with explicit evidence;
- review agent outputs for confidence, contradiction, and policy risk;
- generate product briefs and paper-trading research artifacts;
- keep publication, account changes, and live financial actions behind approval.

## Architecture

- **VPS/OpenClaw:** orchestration, tools, storage, and model routing.
- **Jev/TypeSafe:** optional typed Choice, Score, and Boolean/Noul decisions.
- **Galaxy A16:** mobile queue, sensor/input surface, offline cache, and private control UI.
- **GitHub:** source, tests, deployment history, and reviewable changes.
- **Telegram/X:** delivery surfaces only after authentication and publication review.

## Configuration

Copy `config/evez-jev.example.json` into a private runtime configuration and provide credentials through the host secret store. Never commit API keys, bot tokens, SSH credentials, wallet keys, or exchange secrets.

## Revenue lanes

1. Opportunity Scanner: evidence-backed AI and crypto research briefs.
2. Agent Referee: confidence and contradiction checks for automation teams.
3. A16 Companion: offline-first mobile control and queue synchronization.
4. Product Forge: validated briefs into small APIs, reports, and utilities.

Crypto features are research, alerting, and paper-trading only until a separate explicit authorization and exchange-specific safety review exists.

## Acceptance checks

- local queue works without network;
- sync is authenticated and idempotent;
- no secret appears in logs or repository files;
- low-confidence decisions route to review;
- no workflow publishes or trades without a human approval boundary.
