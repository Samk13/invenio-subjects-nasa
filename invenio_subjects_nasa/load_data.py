"""Load raw csv file and clean it up."""
import csv

from invenio_subjects_nasa.utils import logger


def load_data(raw_csv_data):
    """Load data.

    Args:
        row_data (csv): row csv file coming from
        https://www.sti.nasa.gov/nasa-thesaurus/
    """
    with open(raw_csv_data, newline="\n", encoding="utf-8") as raw_csv:
        f = csv.reader(raw_csv)
        # skip header
        next(f, None)
        for row in f:
            logger(row)
            yield clean_row(row)


def write_data(clean_csv, file_name):
    """Write data to csv file.

    Args:
        clean_csv (list): csv row list
        file_name (string): output filename
    """
    with open(file_name, "w", encoding="utf-8") as yaml_f:
        for row in clean_csv:
            print(row, file=yaml_f)


def clean_row(r):
    """Strip out unwanted chars."""
    for index in r:
        return index.replace('"', "").split(",")
