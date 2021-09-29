from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from ..db import crud
from ..dependencies import get_db

router = APIRouter()


@router.get("/countries/", response_model=List[str])
def read_countries(db: Session = Depends(get_db)):
    countries = crud.get_countries(db)
    return [country for (country,) in countries]
