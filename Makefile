.PHONY: help install dev-install test lint format clean build docs run-cli run-web

PYTHON := python3
PIP := pip3

help:
	@echo "Motor de Tradução Universal 0/0"
	@echo ""
	@echo "Available commands:"
	@echo "  install      Install the package"
	@echo "  dev-install  Install with development dependencies"
	@echo "  test         Run tests"
	@echo "  lint         Run linters"
	@echo "  format       Format code"
	@echo "  clean        Clean build artifacts"
	@echo "  build        Build the package"
	@echo "  run-cli      Run CLI demo"
	@echo "  run-web      Run web server"
	@echo ""

install:
	$(PIP) install -e .

dev-install:
	$(PIP) install -e ".[dev,notebooks]"

test:
	pytest tests/ -v --cov=src/universal_translation_00 --cov-report=term-missing

lint:
	ruff check src/ tests/
	mypy src/

format:
	black src/ tests/
	ruff check --fix src/ tests/

clean:
	rm -rf build/ dist/ *.egg-info/
	rm -rf .pytest_cache/ .mypy_cache/ .ruff_cache/
	rm -rf htmlcov/ .coverage
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true

build: clean
	$(PYTHON) -m build

run-cli:
	universal-translate-00 --help

run-web:
	uvicorn universal_translation_00.web.app:app --reload --host 0.0.0.0 --port 8000

# Demo commands
demo-bhagavad-gita:
	./scripts/run_bhagavad_gita_demo.sh

demo-psalm-148:
	./scripts/run_psalm_148_demo.sh

demo-free-text:
	./scripts/run_free_text_demo.sh

# Data processing
rebuild-data:
	$(PYTHON) scripts/rebuild_processed_data.py

generate-dict00:
	$(PYTHON) scripts/generate_dict00_from_source.py
