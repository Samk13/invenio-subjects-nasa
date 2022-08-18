import click

from invenio_subjects_nasa.converter import csv_to_yaml
from invenio_subjects_nasa.load_data import load_data
from invenio_subjects_nasa.utils import logger

row_data = "invenio_subjects_nasa/downloads/thesaurus-CSV.csv"
output_yaml = "invenio_subjects_nasa/vocabularies/nasa_thesaurus.yaml"


@click.command()
def main():
    """initiate the app"""
    for row in load_data(row_data):
        logger(row)
        csv_to_yaml(row, output_yaml)


if __name__ == "__main__":
    main()
