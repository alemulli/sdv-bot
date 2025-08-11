FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the app
COPY . .

# store persistent state on the mounted volume (set in fly.toml)
ENV BUNDLES_STATE_PATH=/data/bundles_state.json

CMD ["python", "main.py"]
