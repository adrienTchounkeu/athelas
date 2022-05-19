from typing import Any, List
from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
    Form,
    UploadFile,
    File,
)
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps

router = APIRouter()


@router.post(
    "/",
    response_model=schemas.UserSchema,
    status_code=status.HTTP_201_CREATED,
)
def create_user(
    *,
    db: Session = Depends(deps.get_db),
    user_in: schemas.UserCreate,
) -> Any:
    """
    Create new user.
    """
    user = crud.user.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system.",
        )
    user = crud.user.create(db, obj_in=user_in)
    return user


@router.post("/file-upload", response_model=schemas.Image)
async def upload_file(
    *,
    db: Session = Depends(deps.get_db),
    image: UploadFile = File(...),
) -> Any:
    image_o = await crud.user.upload_file(
        db,
        image=image,
    )

    if image_o:
        return image_o

    raise HTTPException(
        status_code=400,
        detail="Error while uploading the image",
    )
