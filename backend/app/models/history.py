from datetime import datetime
from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    DateTime,
)

from app.db.base_class import Base


class History(Base):
    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey('user.id'),
        nullable=False,
    )

    original_image_id = Column(
        Integer,
        ForeignKey('image.id'),
        nullable=False,
    )

    modified_image_id = Column(
        Integer,
        ForeignKey('image.id'),
        nullable=False,
    )

    uploaded_date = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )
