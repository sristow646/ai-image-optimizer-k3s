FROM python:3.10-slim AS builder

WORKDIR /app
COPY requirements.txt .
RUN apt-get update && apt-get install -y --no-install-recommends build-essential && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get purge -y build-essential && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

# Final stage
FROM python:3.10-slim

WORKDIR /app
COPY --from=builder /usr/local/lib/python3.10 /usr/local/lib/python3.10
COPY --from=builder /usr/local/bin /usr/local/bin
COPY . .

EXPOSE 7860
CMD ["python", "app.py"]
