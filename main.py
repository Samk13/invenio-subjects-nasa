import click

from invenio_subjects_nasa.converter import csv_to_yaml
from invenio_subjects_nasa.load_data import load_data
from invenio_subjects_nasa.write_data import write_data

# row_data = "invenio_subjects_nasa/downloads/thesaurus-CSV.csv"
row_data = "invenio_subjects_nasa/downloads/nasa_xs_test.csv"

clean_csv_input = "invenio_subjects_nasa/vocabularies/test_xs_nasa.csv"
output_yaml = "invenio_subjects_nasa/vocabularies/nasa_test_xs_thesaurus.yaml"


@click.command()
def main():
    """initiate the app"""
    cleaned_csv = load_data(row_data)
    write_data(cleaned_csv)
    csv_to_yaml(clean_csv_input, output_yaml)


if __name__ == "__main__":
    main()
