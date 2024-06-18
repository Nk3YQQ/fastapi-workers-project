import pytest

from app.settings import TEST_ENGINE
from models.session import Session

engine_test = TEST_ENGINE

get_db = Session(engine_test).get_session()


@pytest.fixture(scope="module")
def client(db):
    def override_get_db():
        try:
            yield db
        finally:
            db.close()
