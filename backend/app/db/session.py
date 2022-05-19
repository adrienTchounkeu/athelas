from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from app.core.config import settings


engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URI,
    pool_pre_ping=True,
)
SessionLocal = scoped_session(sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
))

SQLALCHEMY_DATABASE_TEST_URL = settings.SQLALCHEMY_TEST_DATABASE_URI

test_engine = create_engine(
    SQLALCHEMY_DATABASE_TEST_URL,
    pool_pre_ping=True,
)

TestingSessionLocal = scoped_session(sessionmaker(bind=test_engine))
