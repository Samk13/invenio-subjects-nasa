# invenio-subjects-nasa

NASA thesaurus subject terms for InvenioRDM
This package is inspired by [invenio-subjects-mesh](https://github.com/galterlibrary/invenio-subjects-mesh)
Install this extension to get NASA thesaurus subject terms used to index and retrieve materials in the STI Repository into your instance.

## Installation

From your instance active venv:
```console
pip install invenio-subjects-nasa==1.0.0
```

This will add it to your Pipfile.

you can double check by running
```console
pip freeze | grep invenio-subjects-nasa
```
in your invenio instance run:
```console
invenio rdm-records fixtures
invenio-cli run
```

### Versions

This repository follows [SemVer versioning](https://semver.org/):


## Usage

There are 2 types of users for this package. Maintainers of the package and instance administrators.

### Instance administrators

For instance administrators, after you have installed the extension as per the steps above,
please read [Invenio subjects documentation](https://inveniordm.docs.cern.ch/customize/vocabularies/subjects/)

**Note**

There is always a room for improvements specially the performance, feel free to drop a PR for that.
TODO:
- write more tests
- improve performance, maybe using Pandas or numpy instead, etc ...


## Future Ideas

- InvenioRDM doesn't have a way to update pre-existing subjects yet. Once there is one,
  this package should provide the functionality to update NASA terms.