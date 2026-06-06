FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    curl ca-certificates \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir \
    fastapi>=0.110 \
    uvicorn[standard]>=0.29 \
    httpx>=0.27 \
    pydantic>=2.0 \
    aiofiles>=23.0

COPY evez_gateway.py .
COPY openclaw.json .

ENV PORT=8080
EXPOSE 8080

# Health check built-in
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD curl -f http://localhost:8080/health || exit 1

CMD ["uvicorn", "evez_gateway:app", "--host", "0.0.0.0", "--port", "8080", "--workers", "2", "--loop", "uvloop"]
