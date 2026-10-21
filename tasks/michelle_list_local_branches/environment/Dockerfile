FROM python:3.12-slim-bookworm

RUN apt-get update \
    && apt-get install -y --no-install-recommends git \
    && rm -rf /var/lib/apt/lists/* \
    && python -m pip install --no-cache-dir pytest==9.1.1

WORKDIR /app/repo
COPY README.md /app/repo/README.md

RUN git init --initial-branch=main \
    && git config user.name "Task Author" \
    && git config user.email "task-author@example.com" \
    && git add README.md \
    && git commit -m "Initialize branch practice repository" \
    && git branch bugfix/typo \
    && git branch docs/setup \
    && git branch feature/readme \
    && git update-ref refs/remotes/origin/main HEAD \
    && git update-ref refs/remotes/origin/remote-only HEAD
