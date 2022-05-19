from factory.alchemy import SQLAlchemyModelFactory
from faker import Factory as FakerFactory

from app.db.session import TestingSessionLocal

ffactory = FakerFactory.create(locale='en_US')


class BaseFactory(SQLAlchemyModelFactory):
    class Meta:
        abstract = True
        sqlalchemy_session = TestingSessionLocal
