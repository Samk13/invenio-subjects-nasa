"""Convert from csv to yaml."""

import yaml


def generate_id(csv_row):
    """Build id from Key UID Relationship Type and Related UID."""
    ki = csv_row[0] # Key UID
    rt = csv_row[3] # Relationship Type
    ru = csv_row[4] # Related UID
    return f"{ki}-{rt}-{ru}"


def nasa_schema(csv_obj):
    """Return a dictionary with the schema for Invenio names."""
    return [
        {
            "id": str(generate_id(csv_obj)),
            "scheme": str(csv_obj[6]), # Related Object Class
            "subject": str(csv_obj[5]), # Related Descriptor
        }
    ]


def csv_to_yaml(csv_row, yaml_file, schema=nasa_schema):
    """Convert a csv file to a yaml file¨based on given schema."""
    with open(yaml_file, "a", encoding="utf-8") as yaml_f:
        # for row in to_yaml:
        yaml.dump(schema(csv_row), yaml_f)
