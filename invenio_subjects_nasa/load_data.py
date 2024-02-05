# -*- coding: utf-8 -*-
#
# Copyright (C) 2022-2024 KTH Royal Institute of Technology.
#
# invenio-subjects-nasa is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.

"""Load raw csv file and clean it up."""
import ast


def load_data(raw_csv_data):
    """Load data.

    Args:
        row_data (csv): row csv file downloaded from
        https://www.sti.nasa.gov/nasa-thesaurus/
    """
    with open(raw_csv_data, newline="\n", encoding="utf-8") as raw_csv:
        # skip header
        next(raw_csv, None)
        for row in raw_csv:
            yield ast.literal_eval(row).split(",")
