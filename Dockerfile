FROM python:3.12.2-slim

# `uv` dependencies
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Install `uv`
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# Add `uv` to path
ENV PATH="/root/.local/bin:$PATH"

# working directory
WORKDIR /app

# copying project files inside docker
COPY pyproject.toml .env ./

# install project dependencies
RUN uv sync
ENV PATH="/app/.venv/bin/:$PATH"

CMD ["fastapi", "run", "src/main.py"]
# CMD ["sleep", "3000"] # for debugging purposes
