import click
from .load_data import load_data
from .write_data import write_data
from .converter import csv_to_yaml

# row_data = "nasa_vocabularies/nasa_controlled_vocabularies/downloads/thesaurus-CSV.csv"
row_data = "nasa_vocabularies/nasa_controlled_vocabularies/downloads/nasa_test.csv"
# output_file = (
#     "nasa_voc/nasa_controlled_vocabularies/vocabularies/clean_thesaurus_CSV.csv"
# )
clean_csv_input = "nasa_vocabularies/nasa_controlled_vocabularies/vocabularies/subjects_nasa.csv"
output_yaml = "nasa_vocabularies/nasa_controlled_vocabularies/vocabularies/out_yaml_1.yaml"


@click.command()
def main():
    """initiate the app"""
    cleaned_csv = load_data(row_data)
    write_data(cleaned_csv)
    csv_to_yaml(clean_csv_input, output_yaml)


if __name__ == "__main__":
    main()
