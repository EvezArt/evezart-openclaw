FROM node:22-bookworm-slim

# Install system deps
RUN apt-get update && apt-get install -y \
    curl git python3 python3-pip sqlite3 ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Install Bun
RUN curl -fsSL https://bun.sh/install | bash
ENV PATH="/root/.bun/bin:${PATH}"

# Enable pnpm
RUN corepack enable && corepack prepare pnpm@latest --activate

WORKDIR /app

# Copy openclaw fork (pre-built from EvezArt/openclaw-fork)
# We pull directly from npm registry
RUN npm install -g openclaw 2>/dev/null || \
    npx --yes openclaw@latest --version 2>/dev/null || \
    echo "openclaw install from npm attempted"

# Copy our personalized config and workspace
COPY config/openclaw.json /root/.openclaw/openclaw.json
COPY workspace/ /root/.openclaw/workspace/
COPY skills/ /root/.openclaw/skills/
COPY hooks/ /root/.openclaw/hooks/

# Copy spine init
COPY spine/init.jsonl /root/.openclaw/spine.jsonl 2>/dev/null || true

# Install Python skills deps
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt || true

# Create data directory
RUN mkdir -p /root/.openclaw/backup /root/.openclaw/logs

ENV NODE_ENV=production
ENV OPENCLAW_CONFIG_DIR=/root/.openclaw
ENV HOME=/root
ENV PORT=8080

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
    CMD curl -f http://localhost:${PORT}/health || exit 1

EXPOSE 8080 18789 18790

# Entrypoint: try openclaw gateway first, fallback to our own server
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
CMD ["/entrypoint.sh"]
