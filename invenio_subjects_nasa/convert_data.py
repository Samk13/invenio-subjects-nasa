#
# Copyright (C) 2022-2024 KTH Royal Institute of Technology.
#
# invenio-subjects-nasa is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.

import csv
from io import StringIO

import yaml

from invenio_subjects_nasa.utils import logger


def load_csv_data(filepath: str):
    """Load and parse CSV data, yielding each row as a tuple."""
    try:
        with open(filepath, newline="\n", encoding="utf-8") as file:
            reader = csv.reader(file)

            # Skip the header row
            try:
                next(reader)

            except StopIteration as err:
                # This handles the case where the file is empty
                logger.debug("CSV reading error: '%s'", err)
                return
            except csv.Error as csv_err:
                # Handle potential CSV format errors (less common in just reading the header)
                logger.debug("CSV format error: '%s'", csv_err)
                return

            for row in reader:
                yield from parse_single_string_row(row[0])
                # yield tuple(row[0].replace('"', '').split(','))
    except OSError as io_err:
        # Handle file access errors (e.g., file not found, permission denied)
        logger.debug("File access error: '%s'", io_err)
    except csv.Error as csv_err:
        # Handle general CSV errors that might occur during reading
        logger.debug("CSV reading error: '%s'", csv_err)


def parse_single_string_row(row: str):
    """Parse a single string row from CSV into a tuple.

    row = '64538,"2001 Mars Odyssey","NASA Thesaurus","BT","55662","Mars missions","NASA Thesaurus"'
    """
    # Use StringIO to simulate a file-like object because csv.reader expects a file-like object
    reader = csv.reader(StringIO(row), quotechar='"', delimiter=",")
    # reader: <_csv.reader object at 0x7fd7280271b0>

    for parsed_row in reader:
        # parsed_row = ['64538', '2001 Mars Odyssey', 'NASA Thesaurus', 'BT', '55662', 'Mars missions', 'NASA Thesaurus']
        if not len(parsed_row) == 7:
            logger.debug("Row length is not 7: '%s'", parsed_row)
        yield tuple(parsed_row)
        return  # Ensures the function exits after yielding


def transform_row_to_schema(row: tuple):
    """Transform a CSV row into the desired schema format."""
    return {"id": generate_id(row), "scheme": "NASA Thesaurus", "subject": row[5]}


def generate_id(row: tuple):
    """Generate a unique ID based on CSV row content.

    row[0] = 'Key UID'
    row[3] = 'Relationship Type'
    row[4] = 'Related UID'
    """
    return f"{row[0]}-{row[3]}-{row[4]}"


def remove_duplicates(data: list):
    """Remove duplicate entries based on 'subject'."""
    logger.debug("Removing duplicate entries...")
    seen = set()
    unique_data = []

    for item in data:
        if item["subject"] not in seen:
            seen.add(item["subject"])
            unique_data.append(item)
        # logger.debug("%s is a duplicate", item["subject"])

    sorted_unique_data = sorted(unique_data, key=lambda x: x["id"])
    return sorted_unique_data


def write_to_yaml(data: list, filepath: str):
    """Write data to a YAML file."""
    logger.debug("Writing data to YAML file...")

    with open(filepath, "w", encoding="utf-8") as file:
        yaml.dump(data, file)


def main(csv_filepath_input: str, yaml_filepath_output: str):
    """Main function to process CSV data and write it to a YAML file."""
    data = load_csv_data(csv_filepath_input)
    transformed_data = [transform_row_to_schema(row) for row in data]
    unique_data = remove_duplicates(transformed_data)
    write_to_yaml(unique_data, yaml_filepath_output)
