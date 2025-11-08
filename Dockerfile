FROM python:3.11-slim-buster
WORKDIR /app

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Copy project files
COPY . /app

# Install dependencies using uv
RUN uv sync --frozen

CMD ["uv", "run", "python", "main.py"]
