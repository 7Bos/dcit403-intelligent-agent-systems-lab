FROM python:3.12.3-slim

RUN apt-get update && apt-get install -y \
    prosody \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
