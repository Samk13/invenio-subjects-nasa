import click

from invenio_subjects_nasa.converter import csv_to_yaml, write_to_disk
from invenio_subjects_nasa.load_data import load_data

row_data = "invenio_subjects_nasa/downloads/thesaurus-CSV.csv"
output_yaml = "invenio_subjects_nasa/vocabularies/nasa_thesaurus.yaml"


@click.command()
def main():
    """initiate the app"""
    res = []
    for row in load_data(row_data):
        res.append(csv_to_yaml(row))
    write_to_disk(res, output_yaml)


if __name__ == "__main__":
    main()
