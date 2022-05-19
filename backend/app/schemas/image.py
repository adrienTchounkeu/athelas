from datetime import datetime

from pydantic import BaseModel
from typing import Optional


class Image(BaseModel):
    bucket: str
    file_name: str
    uploaded_date: datetime
    wrinkle: Optional[bool]

    class Config:
        orm_mode = True
