from typing import (
    Any,
    Dict,
    Optional,
    Union,
)
from sqlalchemy.orm import Session
from fastapi import UploadFile
import uuid

from app.crud.base import CRUDBase
from app.models.user import User
from app.models.image import Image
from app.schemas.user import (
    UserCreate,
    UserUpdate,
)


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def get_by_email(self, db: Session, *, email: str) -> Optional[User]:
        return db.query(User).filter(
            User.email == email.lower()
        ).first()

    def create(self, db: Session, *, obj_in: UserCreate) -> User:
        db_obj = User(
            email=obj_in.email,
            firstname=obj_in.first_name,
            lastname=obj_in.last_name,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    async def upload_file(
        self,
        db: Session,
        image: UploadFile,
    ) -> Image:
        '''
        - remove spaces in the file name in case there are
        - ensure that the bucket name is unique
        '''

        file_name_without_spaces = "_".join(image.filename.split())

        # generate bucket name
        bucket = f"{uuid.uuid4()}_{file_name_without_spaces}"

        try:
            path = f"wrinkle_images/{bucket}"
            with open(path, 'wb') as f:
                data = await image.read()
                f.write(data)
                f.close()
        except BaseException:
            # return value in case impossible to write the image
            return None
        else:
            image = Image(
                bucket=bucket,
                file_name=image.filename,
                wrinkle=False,
            )
            db.add(image)
            db.commit()
            db.refresh(image)
            return image


user = CRUDUser(User)
