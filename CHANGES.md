# Changes

v2.1.0 (released 2025-09-17)

- **BREAKING**: Migrate from setup.cfg to pyproject.toml for modern Python packaging
- Replace setuptools with Hatchling as build backend for faster builds
- Replace black + isort + flake8 with Ruff for unified code formatting and linting
- Add dynamic versioning, version now derived from __init__.py automatically
- Abstract CSV filename to configurable variable (NASA_THESAURUS_CSV_FILENAME)
- Update NASA thesaurus data from 2024-02-05 to 2025-09-17
- Modernize GitHub Actions workflows to use uv package manager
- Update CI/CD pipelines for improved performance and reliability
- Remove legacy setup.py and setup.cfg files
- Update all tooling to use modern Python packaging standards (PEP 518/621)

v2.0.2 (released 2024-02-07)

- Fix pypi deployment
- Update README.md

v2.0.0 (released 2024-02-07)

- Add GitHub actions for tests and pypi deployment
- Add Makefile and update setup.cfg and setup.py
- Update controlled vocabulary to 2024-02-07
- remove unused files and dependencies
- Add support for InvenioRDM v12.0.0
- Update license to the package
- Add tests for the package
- Update requirements
- sort terms by id

v1.1.2 (released 2022-08-18)

- Initial public release.
