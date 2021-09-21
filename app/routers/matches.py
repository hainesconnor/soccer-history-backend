from typing import List

from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from ..db import crud, models, schemas
from .. dependencies import get_db, oauth2_scheme

router = APIRouter()

@router.get("/matches/", response_model=List[schemas.Match])
def read_matches(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    matches = crud.get_matches(db, skip=skip, limit=limit)
    return matches

@router.get("/matches_test/", response_model=List[schemas.Match])
def read_matches(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    matches = crud.get_matches(db, skip=skip, limit=limit)
    return matches