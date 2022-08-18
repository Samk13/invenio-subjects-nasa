"""Write data to yaml."""
from pathlib import Path


def write_data(
    clean_csv, file_name=Path(
        __file__
    ).parent / "vocabularies/subjects_nasa.csv"
):
    """Write data to csv file.

    Args:
        Clean_csv (list): csv row list entries
        file_name (string): output filename.
    """
    with open(file_name, "w", encoding="utf-8") as yaml_f:
        for row in clean_csv:
            print(row, file=yaml_f)
