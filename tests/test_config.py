from pathlib import Path

from invenio_subjects_nasa import config


def test_nasa_subjects_csv_input_path():
    """Test the default value of the NASA subjects CSV input path."""
    assert config.nasa_subjects_csv_input_path == (
        Path.cwd()
        / "invenio_subjects_nasa"
        / "downloads"
        / config.NASA_THESAURUS_CSV_FILENAME
    )


def test_nasa_subjects_yaml_output_path():
    """Test the default value of the NASA subjects YAML output path."""
    assert config.nasa_subjects_yaml_output_path == (
        Path.cwd() / "invenio_subjects_nasa" / "vocabularies" / "nasa_thesaurus.yaml"
    )
