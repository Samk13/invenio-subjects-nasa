# invenio-subjects-nasa

NASA thesaurus subject terms for InvenioRDM

Install this extension to get NASA NASA subject terms used to index and retrieve materials in the STI Repository into your instance.

## Installation

From your instance active venv:
go to the where you cloned the repo:

    pipenv install .

This will add it to your Pipfile.

double check by running
pip freeze

### Versions

This repository follows [calendar versioning](https://calver.org/):

`2021.08.18` is both a valid semantic version and an indicator of the year-month corresponding to the loaded NASA terms.


## Usage

There are 2 types of users for this package. Maintainers of the package and instance administrators.

### Instance administrators

For instance administrators, after you have installed the extension as per the steps above, you need to run:
invenio rdm-records fixtures
invenio-cli run

please read [Invenio documentation](https://inveniordm.docs.cern.ch/customize/vocabularies/subjects/)

**Note**

There is always a room for improvement in this package specially the performance feel free to drop a PR for that.


## Future Ideas

- InvenioRDM doesn't have a way to update pre-existing subjects yet. Once there is one,
  this package should provide the functionality to update NASA terms.