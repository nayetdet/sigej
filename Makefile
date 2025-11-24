.PHONY: install run seed

install:
	uv sync --all-groups

run:
	uv run python -m src.sigej.main

seed:
	uv run python -m scripts.seed
