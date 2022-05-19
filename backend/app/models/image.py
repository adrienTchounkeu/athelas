from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Boolean,
)

from app.db.base_class import Base


class Image(Base):
    id = Column(Integer, primary_key=True, index=True)

    bucket = Column(String)
    file_name = Column(String)
    uploaded_date = Column(
        DateTime,
        default=datetime.utcnow,
    )
    wrinkle = Column(Boolean)
