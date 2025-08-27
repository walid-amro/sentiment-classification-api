#!/bin/bash

git clone https://github.com/walid-amro/sentiment-classification-api
cd sentiment-classification-api
uv self update
uv sync
source .venv/bin/activate
vllm serve --port 8001 clapAI/modernBERT-base-multilingual-sentiment & 
vllm serve --port 8002 CAMeL-Lab/bert-base-arabic-camelbert-mix-sentiment &
uv run --env-file .env run-api-server
