import pytest
import os

from dotenv import load_dotenv
from utilities.data_reader import TestDataReader
from utilities.config_reader import ConfigReader
from utilities.schema_validator import SchemaValidator

from apis.clinics_client import ClinicsClient
from apis.appointments_client import AppointmentsClient

@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()  # loads variables from .env into environment
    return {
        "env": os.getenv("TEST_ENV_NAME"),
        "browser": os.getenv("BROWSER")
    }

@pytest.fixture(scope="session")
def test_data_reader(load_env):
    file_path = os.path.join(os.path.dirname(__file__),"testdata")
    file_name = "data.json"
    reader = TestDataReader(os.path.join(file_path, file_name), load_env.get("env"))
    return reader.load_data()

@pytest.fixture(scope="session")
def config_data_reader(load_env):
    file_path = os.path.join(os.path.dirname(__file__),"config")
    file_name = "config.json"
    reader = ConfigReader(os.path.join(file_path, file_name), load_env.get("env"))
    return reader.load_data()

@pytest.fixture(scope="session")
def clinics_client(config_data_reader):
    return ClinicsClient(config_data_reader.get("url"))

@pytest.fixture
def validator():
    return SchemaValidator()

@pytest.fixture(scope="session")
def appointments_client(config_data_reader):
    return AppointmentsClient(config_data_reader.get("url"))