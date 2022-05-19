from typing import Generator

import pytest
from fastapi.testclient import TestClient

import app.tests.testing_env  # NOQA
from app.main import app

from app.db.base_class import Base
from sqlalchemy_utils import create_database, database_exists, drop_database
from app.api.deps import get_db

from app.db.session import (
    TestingSessionLocal,
    SQLALCHEMY_DATABASE_TEST_URL,
    test_engine,
)
from app.core.config import settings


'''
EXTREMELY IMPORTANT!!!
PREVENTS TEST API CALLS ACCESSING PRODUCTION DATA
'''


def override_get_db():
    try:
        db = TestingSessionLocal
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

'''
END OF OVERRIDE SECTION
'''


@pytest.fixture(scope='session', autouse=True)
def db_schema():
    """
    Clean up, in case tables were left around from a previous run.
    This can happen if the test process was abruptly killed.
    """
    if database_exists(SQLALCHEMY_DATABASE_TEST_URL):
        drop_database(SQLALCHEMY_DATABASE_TEST_URL)

    create_database(SQLALCHEMY_DATABASE_TEST_URL)
    Base.metadata.create_all(bind=test_engine)

    yield

    drop_database(SQLALCHEMY_DATABASE_TEST_URL)


@pytest.fixture(scope='function')
def db() -> Generator:
    sess = TestingSessionLocal()

    yield sess

    for table in reversed(Base.metadata.sorted_tables):
        sess.connection().execute(table.delete())


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c
