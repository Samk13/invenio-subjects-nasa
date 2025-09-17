# invenio-subjects-nasa

![Tests](https://github.com/Samk13/invenio-subjects-nasa/actions/workflows/tests.yml/badge.svg)
![Pypi](https://img.shields.io/pypi/v/invenio-subjects-nasa.svg)
![License](https://img.shields.io/github/license/mashape/apistatus.svg)
[![Downloads](https://static.pepy.tech/badge/invenio-subjects-nasa)](https://pepy.tech/project/invenio-subjects-nasa)

The NASA Thesaurus contains the authorized NASA subject terms used to index and retrieve materials in the STI Repository. The scope of this controlled vocabulary includes not only aerospace engineering, but all supporting areas of engineering and physics, the natural space sciences (astronomy, astrophysics, and planetary science), Earth sciences, and the biological sciences. The NASA Thesaurus contains over 18,400 subject terms, 4,300 definitions, and more than 4,500 USE cross references.

`invenio-subjects-nasa` for [InvenioRDM](https://inveniosoftware.org/products/rdm/) is an extension that provides the NASA thesaurus subject terms used to index and retrieve materials in the STI Repository into your instance.

Please read: [Invenio subjects documentation](https://inveniordm.docs.cern.ch/customize/vocabularies/subjects/)

## Installation

Install the package in your InvenioRDM instance:

```console
pip install invenio-subjects-nasa
```

Add the subjects to your instance:

```console
invenio rdm-records fixtures
```

This will add the NASA subjects to your instance. After completion, you can access the subjects in the deposit page under `Keywords and subjects`.

## Development

### Requirements

- Python >=3.12
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

### Setup

```console
# Clone the repository
git clone https://github.com/Samk13/invenio-subjects-nasa.git
cd invenio-subjects-nasa

# Install dependencies with uv (recommended)
uv pip install -e ".[tests]"
```

### Testing

```console
# Run all tests
make test

# Format code
make format

# Check code quality
make lint
```

### Updating NASA Thesaurus Data

Check for updates at the [NASA Thesaurus](https://sti.nasa.gov/nasa-thesaurus/). 

To update the data:
1. Download the new CSV file to `invenio_subjects_nasa/downloads/`
2. Update the filename in `invenio_subjects_nasa/config.py` (`NASA_THESAURUS_CSV_FILENAME`)
3. Run the conversion:

```console
make run
```

## Release Process

Releases are automated via GitHub Actions. To create a new release:

```bash
# Update version in invenio_subjects_nasa/__init__.py
# Update CHANGES.md with release notes
git tag v2.1.0
git push origin v2.1.0
```

The package will be automatically built and published to PyPI.
