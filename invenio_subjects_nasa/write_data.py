# -*- coding: utf-8 -*-
#
# Copyright (C) 2022-2024 KTH Royal Institute of Technology.
#
# invenio-subjects-nasa is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.

"""Write data to yaml."""
from pathlib import Path


def write_data(
    clean_csv, file_name=Path(__file__).parent / "vocabularies/subjects_nasa.csv"
):
    """Write data to csv file.

    Args:
        clean_csv (list): csv row list entries
        file_name (string): output filename.
    """
    with open(file_name, "w", encoding="utf-8") as yaml_f:
        for row in clean_csv:
            print(row, file=yaml_f)
