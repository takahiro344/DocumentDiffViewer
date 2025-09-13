FROM node:20

WORKDIR /workspaces/DocumentDiffViewer
COPY package*.json ./
RUN npm install
COPY . .

EXPOSE 5173