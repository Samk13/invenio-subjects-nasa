import csv
import yaml
from .utils import logger


def generate_id(csv_row):
    """Build id from Key UID Relationship Type and Related UID"""
    return (
        f"{csv_row['Key UID']}-{csv_row['Relationship Type']}-{csv_row['Related UID']}"
    )


def nasa_schema(csv_obj):
    """return a dictionary with the schema for Invenio names"""
    return [
        {
            "id": str(generate_id(csv_obj)),
            "scheme": str(csv_obj["Related Object Class"]),
            "subject": str(csv_obj["Related Descriptor"]),
        }
    ]


async def csv_to_yaml(csv_file, yaml_file, schema=nasa_schema):
    """convert a csv file to a yaml file¨based on given schema"""
    # read csv file
    to_yaml = []
    with open(csv_file, encoding="utf-8") as csv_f:
        reader = csv.DictReader(csv_f)
        for row in reader:
            logger(row)
            to_yaml.append(schema(row))
    # write yaml file
    with open(yaml_file, "w", encoding="utf-8") as yaml_f:
        for row in to_yaml:
            yaml.dump(row, yaml_f)
