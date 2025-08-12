.PHONY: install lint test

install:
	pip install -r requirements.txt

lint:
	pre-commit run --files $(shell git ls-files '*.py')

test:
        PYTHONPATH=src pytest
