from pathlib import Path
from .acr_harmonized_data_model import *

THIS_PATH = Path(__file__).parent

SCHEMA_DIRECTORY = THIS_PATH.parent / "schema"
MAIN_SCHEMA_PATH = SCHEMA_DIRECTORY / "acr_harmonized_data_model.yaml"
