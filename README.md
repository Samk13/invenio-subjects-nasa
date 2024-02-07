# invenio-subjects-nasa

![Tests](https://github.com/Samk13/invenio-subjects-nasa/actions/workflows/tests.yml/badge.svg)

The NASA Thesaurus contains the authorized NASA subject terms used to index and retrieve materials in the STI Repository launch . The scope of this controlled vocabulary includes not only aerospace engineering, but all supporting areas of engineering and physics, the natural space sciences (astronomy, astrophysics, and planetary science), Earth sciences, and the biological sciences. The NASA Thesaurus contains over 18,400 subject terms, 4,300 definitions, and more than 4,500 USE cross references.

`invenio-subjects-nasa` for [InvenioRDM](https://inveniosoftware.org/products/rdm/) is an extension that provides the NASA thesaurus subject terms used to index and retrieve materials in the STI Repository into your instance.
Please read: [Invenio subjects documentation](https://inveniordm.docs.cern.ch/customize/vocabularies/subjects/)

## Installation

First, you need to install the package in your invenio instance.

```console
pip install invenio-subjects-nasa
```

Then, you need to add the subjects to your instance by running the following command:

```console
invenio rdm-records fixtures
invenio-cli run
```

This will add the NASA subjects to your instance, it can take a while to finish.
After that, you can check the subjects in your instance by going to the deposit page under `Keywords and subjects`.

### Versions

This repository follows [SemVer versioning](https://semver.org/):

## Usage

There are 2 types of users for this package. Maintainers of the package and instance administrators.

### Maintainers

### testing

```console
make install
make test
```

You can check if there are updates on the terms by checking the [NASA Thesaurus](https://sti.nasa.gov/nasa-thesaurus/).
If there are updates, you can download the csv file in the download folder and run the following command:

```console
make run
```

### Upload to pypi

Publishing will be done automatically by GitHub actions when a new tag is created.

```bash
git tag vX.Y.Z
git push origin master vX.Y.Z
```

### manually upload to pypi

```console
make install-package-tools # this will install twine (install-package-tools-pipenv if you use pipenv)
make package # this will zip the package into dist dir
make package-check # verify if the package pass twine checks

export TWINE_USERNAME=__token__
export TWINE_PASSWORD=pypi-<YOUR_TOKEN>
twine upload dist/*
```
