# -*- coding: utf-8 -*-
#
# Copyright (C) 2022-2024 KTH Royal Institute of Technology.
#
# invenio-subjects-nasa is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.
"""Nasa subject terms for InvenioRDM"""

from invenio_subjects_nasa.converter import csv_to_yaml, write_to_disk
from invenio_subjects_nasa.load_data import load_data
from invenio_subjects_nasa.utils import logger

row_data = "invenio_subjects_nasa/downloads/thesaurus-CSV.csv"
output_yaml = "invenio_subjects_nasa/vocabularies/nasa_thesaurus.yaml"


def main():
    """initiate the app"""
    logger("Converting ...")
    res = []
    for row in load_data(row_data):
        res.append(csv_to_yaml(row))
    write_to_disk(res, output_yaml)
    logger("Subjects is been converted successfully!")


if __name__ == "__main__":
    main()
