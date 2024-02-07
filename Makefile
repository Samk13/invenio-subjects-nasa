.DEFAULT_GOAL=ls

ls: # List available commands
	@grep '^[^#[:space:]].*:' Makefile

freeze: # Show installed dependencies
	@pip freeze

format: # Black format and isort imports
	@black . && isort .

install: # Install py dependencies
	@pip install -e ".[tests]"

run: # Fetch data, convert it to yaml, and then save it in invenio_subjects_nasa/vocabularies/nasa_voc.yaml
	@DEBUGGER=True python main.py

test: # Run tests
	@bash run-tests.sh

install-package-tools: # Install twine
	@pip install twine

package: # Package to tar.gz file for uploading to pypi
	@python setup.py sdist

package-check: # Check package if it pass pypi tests
	@twine check dist/*
