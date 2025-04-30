init:
	bash install.sh
	uv sync

format:
	uvx ruff check

test:
	uv run pytest
