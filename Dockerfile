# ─────────────────────────────────────────────────────────────────────────────
# LUMINARK Unified API — Dockerfile
# Meridian Axiom Alignment Technologies
# ─────────────────────────────────────────────────────────────────────────────
#
# Build:    docker build -t luminark-api .
# Run:      docker run -p 8000:8000 luminark-api
# Dev:      docker run -p 8000:8000 -v $(pwd):/app luminark-api
#
# The container exposes the FastAPI server at http://localhost:8000
# Interactive API docs: http://localhost:8000/docs
# ─────────────────────────────────────────────────────────────────────────────

FROM python:3.11-slim

# ── metadata ──────────────────────────────────────────────────────────────────
LABEL maintainer="info.rstanfield@gmail.com"
LABEL description="LUMINARK Unified API — Predictive Stage Intelligence"
LABEL version="1.0.0"

# ── system setup ──────────────────────────────────────────────────────────────
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8000

WORKDIR /app

# ── install Python dependencies ───────────────────────────────────────────────
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ── copy application files ────────────────────────────────────────────────────
COPY main.py .
COPY LUMINARK_CONSCIOUSNESS_ENGINE_OMEGA.py .
COPY LUMINARK_OVERWATCH_PRIME_ULTRA.py .

# ── optional: copy test suite ─────────────────────────────────────────────────
COPY test_omega.py .

# ── expose port ───────────────────────────────────────────────────────────────
EXPOSE 8000

# ── health check ──────────────────────────────────────────────────────────────
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" \
    || exit 1

# ── start server ──────────────────────────────────────────────────────────────
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
