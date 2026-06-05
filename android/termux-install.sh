#!/data/data/com.termux/files/usr/bin/bash
# EvezArt OpenClaw — Samsung Galaxy A16 / Termux Install
# Run in Termux: bash termux-install.sh

set -e

EVEZ_DIR="$HOME/.openclaw"
REPO="https://github.com/EvezArt/game-agent-infra.git"

echo "╔══════════════════════════════════════════════════╗"
echo "║  EvezArt OpenClaw — Samsung Galaxy A16 Setup     ║"
echo "╚══════════════════════════════════════════════════╝"

# Update packages
pkg update -y && pkg upgrade -y
pkg install -y python git curl wget

# Install pip packages
pip install fastapi uvicorn httpx pydantic aiofiles --quiet

# Create dirs
mkdir -p "$EVEZ_DIR/workspace" "$EVEZ_DIR/logs" "$EVEZ_DIR/backup" "$EVEZ_DIR/skills"

# Clone workspace from GitHub
if [ -n "$GITHUB_TOKEN" ]; then
    echo "[+] Syncing workspace from GitHub..."
    cd "$HOME"
    git clone "https://$GITHUB_TOKEN@github.com/EvezArt/game-agent-infra.git" evez-infra --depth=1 2>/dev/null || true
    cp -r evez-infra/workspace/* "$EVEZ_DIR/workspace/" 2>/dev/null || true
    cp evez-infra/spine.jsonl "$EVEZ_DIR/spine.jsonl" 2>/dev/null || true
fi

# Download gateway server
echo "[+] Downloading EvezArt gateway..."
curl -sL "https://raw.githubusercontent.com/EvezArt/game-agent-infra/main/evez_gateway.py" \
    -o "$EVEZ_DIR/evez_gateway.py" 2>/dev/null || \
    echo "Note: Download failed, use local copy"

# Install Ollama for local models (optional)
echo ""
echo "[?] Install Ollama for LOCAL on-device models? (y/n)"
read -r INSTALL_OLLAMA
if [ "$INSTALL_OLLAMA" = "y" ]; then
    pkg install -y ollama 2>/dev/null || \
    curl -fsSL https://ollama.com/install.sh | sh 2>/dev/null || \
    echo "Note: Ollama not available in Termux — use cloud providers"
fi

# Create .env file
cat > "$EVEZ_DIR/.env" << 'EOF'
# EvezArt OpenClaw — Environment
# Fill in your keys below

GROQ_API_KEY=YOUR_GROQ_KEY_HERE
OPENROUTER_API_KEY=YOUR_OPENROUTER_KEY_HERE
CEREBRAS_API_KEY=YOUR_CEREBRAS_KEY_HERE
HUGGING_FACE_ACCESS_TOKEN=YOUR_HF_TOKEN_HERE
GATEWAY_TOKEN=evezart-mobile-token
GITHUB_TOKEN=
TELEGRAM_BOT_TOKEN=
TELEGRAM_CHAT_ID=
PORT=8080
EOF

echo "[+] Created .env at $EVEZ_DIR/.env"

# Create autorun script for Termux:Boot
mkdir -p "$HOME/.termux/boot"
cat > "$HOME/.termux/boot/evezart-boot.sh" << 'EOF'
#!/data/data/com.termux/files/usr/bin/bash
# EvezArt OpenClaw — Auto-start on Samsung Galaxy A16

sleep 5  # Wait for network

EVEZ_DIR="$HOME/.openclaw"
source "$EVEZ_DIR/.env" 2>/dev/null

# Start EvezArt gateway in background
cd "$EVEZ_DIR"
nohup python evez_gateway.py >> "$EVEZ_DIR/logs/gateway.log" 2>&1 &
echo "[$(date)] EvezArt OpenClaw started (PID $!)" >> "$EVEZ_DIR/logs/boot.log"
EOF
chmod +x "$HOME/.termux/boot/evezart-boot.sh"

# Create start script
cat > "$HOME/evezart" << 'EOF'
#!/data/data/com.termux/files/usr/bin/bash
EVEZ_DIR="$HOME/.openclaw"
source "$EVEZ_DIR/.env" 2>/dev/null
cd "$EVEZ_DIR"
python evez_gateway.py
EOF
chmod +x "$HOME/evezart"

# Create shortcut scripts
cat > "$HOME/evez-status" << 'EOF'
#!/data/data/com.termux/files/usr/bin/bash
curl -s http://localhost:8080/status | python -m json.tool 2>/dev/null || echo "EvezArt offline"
EOF
chmod +x "$HOME/evez-status"

# PWA installer helper
cat > "$EVEZ_DIR/pwa-install.html" << 'EOF'
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>EvezArt OpenClaw</title>
<link rel="manifest" href="/manifest.json">
<meta name="theme-color" content="#0d0d0d">
</head>
<body style="background:#0d0d0d;color:#00ff88;font-family:monospace;padding:20px">
<h1>⚡ EvezArt OpenClaw</h1>
<p>Add to home screen for Samsung Galaxy A16 PWA experience.</p>
<a href="http://localhost:8080" style="color:#00ff88">Open Gateway →</a>
</body>
</html>
EOF

echo ""
echo "╔══════════════════════════════════════════════════╗"
echo "║  INSTALL COMPLETE                                ║"
echo "╠══════════════════════════════════════════════════╣"
echo "║  Run:  ~/evezart          — Start gateway        ║"
echo "║  Run:  ~/evez-status      — Check status         ║"
echo "║  Boot: Auto-starts via Termux:Boot               ║"
echo "║  URL:  http://localhost:8080                     ║"
echo "╚══════════════════════════════════════════════════╝"
echo ""
echo "[!] Edit $EVEZ_DIR/.env to add your Telegram + GitHub tokens"
echo ""

# Optional: start now
echo "[?] Start EvezArt OpenClaw now? (y/n)"
read -r START_NOW
if [ "$START_NOW" = "y" ]; then
    source "$EVEZ_DIR/.env"
    cd "$EVEZ_DIR"
    python evez_gateway.py
fi
