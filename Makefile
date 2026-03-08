.PHONY: help install run test lint format build h i r t l f b

help:
	@printf "widget - FastAPI widget service\n\n"
	@printf "Usage:\n"
	@printf "  make <target>\n\n"
	@printf "Targets:\n"
	@printf "  help, h      Show this help menu\n"
	@printf "  install, i   Install app and dev dependencies\n"
	@printf "  run, r       Run the API on localhost:8080\n"
	@printf "  test, t      Run the test suite\n"
	@printf "  lint, l      Run the linter\n"
	@printf "  format, f    Format the codebase\n"
	@printf "  build, b     Compile, test, and build distributions\n"

h: help

install:
	UV_CACHE_DIR=.uv-cache uv sync --dev

i: install

run:
	UV_CACHE_DIR=.uv-cache uv run uvicorn widget.app:app --host 127.0.0.1 --port 8080 --reload

r: run

test:
	UV_CACHE_DIR=.uv-cache uv run pytest

t: test

lint:
	UV_CACHE_DIR=.uv-cache uv run ruff check .

l: lint

format:
	UV_CACHE_DIR=.uv-cache uv run ruff format .

f: format

build: lint
	UV_CACHE_DIR=.uv-cache uv run python -m compileall src tests
	UV_CACHE_DIR=.uv-cache uv run pytest
	UV_CACHE_DIR=.uv-cache uv build

b: build
