from sqlalchemy.orm import Session

from app import crud
from app.schemas.user import UserCreate, UserUpdate
from app.tests.factories import (
    UserFactory,
    ffactory,
)
from app.models import User as UserModel
from app.helpers import UserType


def test_create_user(db: Session):
    user_in_dict = dict(
        firstname=ffactory.text(max_nb_chars=100),
        lastname=ffactory.text(max_nb_chars=100),
        email=ffactory.email(),
    )

    user_in = UserCreate(**user_in_dict)

    user_out = crud.user.create(db, obj_in=user_in)

    for key, val in user_in_dict.items():
        assert getattr(user_out, key) == val


def test_get_user(db: Session):
    user = UserFactory()
    db.add(user)
    db.commit()

    user_out = crud.user.get(db, id=user.id)

    assert user_out == user


def test_user_update(db: Session):
    user = UserFactory()
    db.add(user)
    db.commit()

    user_update_dict = dict(
        firstname=ffactory.text(max_nb_chars=100),
        lastname=ffactory.text(max_nb_chars=100),
        email=ffactory.email(),
    )

    user_in = UserUpdate(**user_update_dict)

    db_user = db.query(UserModel).get(user.id)

    user_out = crud.user.update(db, db_obj=db_user, obj_in=user_in)

    for key, val in user_update_dict.items():
        assert getattr(user_out, key) == val
