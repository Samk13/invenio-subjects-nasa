.DEFAULT_GOAL=ls

ls: # List available commands
	@grep '^[^#[:space:]].*:' Makefile

freeze: # Show installed dependencies
	@uv pip freeze

format: # Format code with ruff
	@ruff format . && ruff check --fix .

lint: # Lint code with ruff
	@ruff check .

install: # Install py dependencies
	@uv pip install -e ".[tests]"

run: # Fetch data, convert it to yaml, and then save it in invenio_subjects_nasa/vocabularies/nasa_voc.yaml
	@DEBUGGER=True python main.py

test: # Run tests
	@bash run-tests.sh

install-package-tools: # Install build tools
	@uv pip install build twine

package: # Package to tar.gz file for uploading to pypi
	@python -m build

package-check: # Check package if it pass pypi tests
	@uv pip install twine --quiet 2>/dev/null || true
	@twine check dist/*
