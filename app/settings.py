import os
from pathlib import Path

from models.engine import PostgresSettings
from models.services import create_engine_url

from dotenv import load_dotenv

load_dotenv()


BASE_DIR = Path(__file__).parent.parent

POSTGRES_SETTINGS = {
    "dialect": "psycopg2",
    "user": os.getenv("POSTGRES_USER"),
    "password": os.getenv("POSTGRES_PASSWORD"),
    "host": os.getenv("POSTGRES_HOST"),
    "db_name": os.getenv("POSTGRES_DB")
}

TEST_DB_SETTINGS = {
    "dialect": "psycopg2",
    "user": os.getenv("TEST_USER"),
    "password": os.getenv("TEST_PASSWORD"),
    "host": os.getenv("TEST_HOST"),
    "db_name": os.getenv("TEST_DB")
}

ENGINE = create_engine_url(PostgresSettings, POSTGRES_SETTINGS)
TEST_ENGINE = create_engine_url(PostgresSettings, TEST_DB_SETTINGS)

DATA_PATH = BASE_DIR / 'data'

CUSTOMERS_DATA_PATH = DATA_PATH / 'customers_data.json'
EMPLOYEES_DATA_PATH = DATA_PATH / 'employees_data.json'
ORDERS_DATA_PATH = DATA_PATH / 'orders_data.json'
