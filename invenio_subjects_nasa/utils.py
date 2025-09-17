#
# Copyright (C) 2022-2024 KTH Royal Institute of Technology.
#
# invenio-subjects-nasa is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.

"""Utils for logging info to console."""

import logging
import os

logging.basicConfig(level=logging.INFO)


# Set up logging
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


# Function to set the logging level based on the DEBUGGER environment variable
def configure_logging():
    """Debugger config."""
    debugger = os.getenv("DEBUGGER", "False").lower()
    if debugger == "true":
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.WARNING)


# Invoke it
configure_logging()
