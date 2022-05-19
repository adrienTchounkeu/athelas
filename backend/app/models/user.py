from datetime import datetime
from email.policy import default
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
)

from app.db.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True)

    firstname = Column(String)
    lastname = Column(String)
    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )
