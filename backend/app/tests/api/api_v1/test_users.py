from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from app.core.config import settings
from app.tests.factories import (
    UserFactory,
    ffactory,
)
from app.schemas import UserSchema
from app.models import User as UserModel
from app.helpers import UserType


def test_read_user(
        client: TestClient, db: Session
) -> None:
    user = UserFactory()
    db.add(user)
    db.commit()

    r = client.get(
        url=f"{settings.API_V1_STR}/user/{user.id}",
    )
    user_res = r.json()

    expected = jsonable_encoder(
        UserSchema(
            id=user.id,
            firstname=user.first_name,
            lastname=user.last_name,
            email=user.email,
            type=user.type,
            created_at=user.created_at,
        )
    )

    assert expected == user_res


def test_read_users(
        client: TestClient, db: Session
):
    NUM_USERS = 2

    users = UserFactory.create_batch(NUM_USERS)
    db.add_all(users)
    db.commit()

    r = client.get(
        url=f"{settings.API_V1_STR}/user/",
    )
    users_res = r.json()

    assert len(users_res) == NUM_USERS

    expected = [
        jsonable_encoder(
            UserSchema(
                id=user.id,
                firstname=user.first_name,
                lastname=user.last_name,
                email=user.email,
                type=user.type,
                created_at=user.created_at,
            )
        ) for user in users
    ]

    assert expected == users_res


def test_update_user(
        client: TestClient, db: Session
):
    user = UserFactory()
    db.add(user)
    db.commit()

    user_dict = dict(
        firstname=ffactory.text(max_nb_chars=100),
        lastname=ffactory.text(max_nb_chars=100),
        email=ffactory.email(),
    )
    user_json = jsonable_encoder(user_dict)

    r = client.put(
        url=f"{settings.API_V1_STR}/user/{user.id}",
        json=user_json,
    )
    user_res = r.json()

    db_user = db.query(UserModel).get(user.id)

    expected = jsonable_encoder(
        UserSchema(
            id=db_user.id,
            firstname=user_dict['firstname'],
            lastname=user_dict['lasname'],
            email=user_dict['email'],
            created_at=db_user.created_at,
        )
    )

    assert expected == user_res


def test_create_user(
        client: TestClient, db: Session
):
    user_dict = dict(
        firstname=ffactory.text(max_nb_chars=100),
        lastname=ffactory.text(max_nb_chars=100),
        email=ffactory.email(),
        password=ffactory.text(max_nb_chars=100),
        type=UserType.NORMAL,
    )
    user_json = jsonable_encoder(user_dict)

    r = client.post(
        url=f"{settings.API_V1_STR}/user/", 
        json=user_json,
    )
    user_res = r.json()

    db_user = db.query(UserModel).one()

    expected = jsonable_encoder(
        UserSchema(
            id=db_user.id,
            firstname=user_dict['firstname'],
            lastname=user_dict['lasname'],
            email=user_dict['email'],
            type=user_dict['type'],
            created_at=db_user.created_at,
            updated_at=user_res['updated_at'],
        )
    )

    assert expected == user_res
