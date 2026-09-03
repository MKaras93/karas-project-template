# AGENTS.md

## Project Overview

Python project template using **uv** (dependency manager), **ruff** (formatter/linter), **pytest** (testing), **pydantic-settings** (config), Docker, and Terraform.

## Commands

| Task | Command |
|---|---|
| Install dependencies | `make install-dependencies` (runs `uv sync --extra dev`) |
| Run tests | `make test` (runs `uv run pytest`) |
| Run all tests | `uv run pytest` |
| Run a single test | `uv run pytest tests/test_main.py::TestExample::test_sum_numbers` |
| Check formatting | `uv run ruff format --check .` |
| Auto-format | `uv run ruff format .` |
| Lint | `uv run ruff check .` |
| Lint (auto-fix) | `uv run ruff check --fix .` |
| Install pre-commit hooks | `make init-pre-commit` |

## Architecture

- **`src/`** — application code (entrypoint: `src/main.py`)
- **`src/settings/`** — pydantic-settings config module; exports a `settings` singleton
- **`tests/`** — pytest tests; import from `src` package (e.g. `from src.main import sum_numbers`)
- **`terraform/`** — Terraform Cloud config (placeholder)
- **`inputs/`, `outputs/`, `local/`** — data/log directories; `local/` and `inputs/local/` are gitignored
- **`.env`** — controls env selection; must have key `env` (e.g. `env = "local"`). Copy from `.env.example`.

## Settings System

`src/settings/__init__.py` uses pydantic-settings to load `.env`. A `Settings` base class is overridden per environment (e.g. `TestSettings` for `env=test`). The active instance is the `settings` singleton exported from the module. The Makefile uses `-include .env`, which silently skips missing files; targets that need env vars depend on a `.env:` rule that auto-copies `.env.example` if `.env` doesn't exist.

## Formatting

Ruff is the sole formatter and linter. There is no type checker (mypy/pyright) configured. CI enforces `ruff check .` and `ruff format --check .` on every push.