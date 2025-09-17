#
# Copyright (C) 2022-2024 KTH Royal Institute of Technology.
#
# invenio-subjects-nasa is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.
"""Nasa subject terms for InvenioRDM."""

from invenio_subjects_nasa.config import (
    nasa_subjects_csv_input_path,
    nasa_subjects_yaml_output_path,
)
from invenio_subjects_nasa.convert_data import main
from invenio_subjects_nasa.utils import logger

if __name__ == "__main__":
    logger.debug("Converting ...")
    main(nasa_subjects_csv_input_path, nasa_subjects_yaml_output_path)
    logger.debug("Subjects is been converted successfully!")
