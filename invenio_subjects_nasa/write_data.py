import json
from pathlib import Path


def write_jsonl(
    entries, filepath=Path(__file__).parent / "vocabularies/subjects_nasa.jsonl"
):
    """Write the MeSH jsonl file.
    Return filepath to written file.
    """
    with open(filepath, "w", encoding="utf-8") as f:
        for entry in entries:
            json.dump(entry, f)
            f.write("\n")

    return filepath


def write_data(
    clean_csv, file_name=Path(__file__).parent / "vocabularies/subjects_nasa.csv"
):
    """write data to csv file

    Args:
        clean_csv (list): csv row list entries
        file_name (string): output filename
    """
    with open(file_name, "w", encoding="utf-8") as yaml_f:
        for row in clean_csv:
            print(row, file=yaml_f)
