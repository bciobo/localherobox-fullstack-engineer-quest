.PHONY: test mypy lint clean dev install dist run docker-image start-db import-csv help


help:
	@echo
	@echo "  test          run tests"
	@echo "  mypy          typecheck using mypy"
	@echo "  lint          lint project using flake8"
	@echo "  autoformat    autoformat files using black"
	@echo "  clean         remove build and python file artifacts"
	@echo "  dev           install in development mode"
	@echo "  install       install without dev dependencies"
	@echo "  dist          build dist packages"
	@echo "  run           run server for development"
	@echo "  docker-image  build Docker image"
	@echo "  start-db      run PostgreSQL in a Docker container"
	@echo "  import-csv    import csv data into db"
	@echo "  help          print this message"
	@echo


ensure-poetry:
	@if ! [ -x $(command -v poetry) ]; then \
		echo "Please install poetry (e.g. pip install poetry)"; \
		exit 1; \
	fi

mypy: ensure-poetry
	poetry run mypy --strict src/

lint: ensure-poetry mypy
	poetry check
	poetry run flake8 src/ tests/

autoformat: ensure-poetry lint
	poetry run black src tests

test: ensure-poetry
	poetry run pytest --cov src/ --strict tests

clean:
	find . -name '*.pyc' -delete
	find . -name __pycache__ -delete
	rm -rf .coverage dist build *.egg-info

dist: ensure-poetry clean
	poetry build
	ls -l dist

dev: ensure-poetry clean
	poetry install

install: ensure-poetry clean
	poetry install --no-dev

run: ensure-poetry clean
	poetry run uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload

docker-image:
	docker build -t lhb-backend:0.1.0 . --no-cache

start-db:
	docker-compose -f ../docker-compose.yml up -d db

import-csv:
	python -m src.cmd.csv_importer
