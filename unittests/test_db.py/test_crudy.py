import pytest

from sqlalchemy.orm.session import Session
from app.db.database import SessionLocal

from app.db import models, crud, schemas
from app import dependencies

from fastapi import APIRouter, Depends, HTTPException, status

from unittests.utils import random_username


@pytest.fixture(scope="module")
def db():
    yield SessionLocal()


# TODO refactor database to include "super users", so these tests can be decoupled
# Currently I'm creating a user, and then using that created user for the additional tests
def test_user_crud(db: Session):
    # Test Create User
    username = random_username()
    user = schemas.UserCreate(
        username=username,
        password="123"
    )
    new_user = crud.create_user(db, user)
    name = new_user.username
    assert name == username
    assert hasattr(new_user, "id")

    # Test Read User
    read_user = crud.get_user_by_username(db, username)
    name = read_user.username
    assert name == username

    # Test Read User by Id
    id = int(read_user.id)
    user_by_id = crud.get_user(db, id)
    user_id = user_by_id.id
    assert user_id == id
