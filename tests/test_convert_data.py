import csv

import yaml

from invenio_subjects_nasa.convert_data import (
    load_csv_data,
    remove_duplicates,
    transform_row_to_schema,
)

expected_schema = {
    "id": str,
    "scheme": "NASA Thesaurus",
    "subject": str,
}


def check_yaml_schema(data):
    """Check if the data has the expected schema."""
    # Define the expected schema keys
    expected_keys = {"id", "scheme", "subject"}

    for item in data:
        if not isinstance(item, dict):
            return False  # Each item should be a dictionary

        if not expected_keys.issubset(item.keys()):
            return False  # Check if all expected keys are present

    return True


def test_convert_csv_to_yaml():
    """Test convert CSV to yaml."""
    yaml_file_path = "tests/test_data/output_test.yaml"
    input_test = "tests/test_data/input_test.csv"
    data = load_csv_data(input_test)
    transformed_data = [transform_row_to_schema(row) for row in data]
    unique_data = remove_duplicates(transformed_data)
    # write_to_yaml(unique_data, yaml_file_path)
    # open the file and check the content
    with open(input_test, encoding="utf-8") as csv_file:
        csv_data = csv.reader(csv_file)
        assert csv_data
        # assert that the csv file has 10 rows
        assert len(list(csv_data)) == 10

    with open(yaml_file_path, encoding="utf-8") as file:
        yaml_data = yaml.safe_load(file)
        assert yaml_data
        # duplicate data and header should be removed
        assert len(yaml_data) == 7
        assert len(unique_data) > 0
        # assert that each yaml_data object == expected_schema
        for item in yaml_data:
            assert len(item.keys()) == 3
            assert item["id"]
            assert item["scheme"] == "NASA Thesaurus"
            assert item["subject"]
            assert isinstance(item["id"], str)
            assert isinstance(item["subject"], str)
            assert isinstance(item["scheme"], str)
