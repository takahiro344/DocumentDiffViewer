FROM python:3.11.7-slim-bullseye

USER root

# Python向けの基本的なツールをインストール
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y build-essential python3-dev curl net-tools lsof && \
    python -m pip install --upgrade pip setuptools wheel && \
    rm -rf /var/lib/apt/lists/*

# Node.js 20.19.0（Vite 7.x の要件を満たす）
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs

WORKDIR /workspaces/DocumentDiffViewer
COPY backend/requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 8000
EXPOSE 5678
EXPOSE 5173
