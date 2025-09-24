# ABOUTME: Multi-stage Dockerfile for Kaspa Tracker Bot
# ABOUTME: Optimized for small size and security with Python 3.12

# Stage 1: Builder for dependencies
FROM python:3.12-slim as builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency files
COPY pyproject.toml ./

# Install uv and dependencies
RUN pip install --no-cache-dir uv && \
    uv lock && \
    uv pip install --system --no-cache -r pyproject.toml

# Stage 2: Runtime
FROM python:3.12-slim

WORKDIR /app

# Create non-root user for security and data directory
RUN useradd -m -u 1000 botuser && \
    mkdir -p /app/data && \
    chown -R botuser:botuser /app && \
    chmod 755 /app/data

# Copy installed packages from builder
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy application code
COPY --chown=botuser:botuser . .

# Switch to non-root user
USER botuser

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    DATABASE_PATH=/app/data/kaspa_tracker.db

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import os; exit(0 if os.path.exists('/app/data/kaspa_tracker.db') else 1)"

# Run the bot
CMD ["python", "run.py"]