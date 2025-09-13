FROM python:3.11.7-slim-bullseye

USER root

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y build-essential python3-dev
RUN python -m pip install --upgrade pip setuptools wheel
RUN rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y curl net-tools lsof

WORKDIR /workspaces/DocumentDiffViewer
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

EXPOSE 8000
EXPOSE 5678
