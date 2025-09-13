FROM python:3.11.7-slim-bullseye

USER root

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y build-essential python3-dev curl net-tools lsof && \
    python -m pip install --upgrade pip setuptools wheel && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /workspaces/DocumentDiffViewer
COPY backend/requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 8000
EXPOSE 5678
