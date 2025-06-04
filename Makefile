lint:
	uvx ruff check

format:
	uvx ruff check --fix

test:
	uv run pytest
