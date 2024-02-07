# -*- coding: utf-8 -*-
#
# Copyright (C) 2022-2024 KTH Royal Institute of Technology.
#
# invenio-subjects-nasa is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.
from pathlib import Path

nasa_subjects_csv_input_path = (
    Path.cwd() / "invenio_subjects_nasa" / "downloads" / "thesaurus-CSV-2024-02-05.csv"
)
nasa_subjects_yaml_output_path = (
    Path.cwd() / "invenio_subjects_nasa" / "vocabularies" / "nasa_thesaurus.yaml"
)
