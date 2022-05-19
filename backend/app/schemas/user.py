from datetime import datetime

from typing import Optional
from pydantic import (
    BaseModel,
    EmailStr,
    validator,
)


class UserBase(BaseModel):
    firstname: Optional[str]
    lastname: Optional[str]
    email: EmailStr

    # convert incoming email into lowercase
    @validator('email')
    def validate_email(cls, v):
        return v.lower()

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    email: Optional[EmailStr] = None


class UserSchema(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime = None
