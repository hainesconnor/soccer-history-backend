from collections import Counter
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..db import crud, schemas
from ..dependencies import get_db
from ..authentication import oauth2_scheme

router = APIRouter()


@router.get("/matches/", response_model=List[schemas.Match])
def read_matches(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    matches = crud.get_matches(db, skip=skip, limit=limit)
    return matches


@router.get("/matches/{country}", response_model=List[schemas.Match])
def read_matches_by_country(country: str, db: Session = Depends(get_db)):
    matches_by_country = crud.get_matches_by_country(country, db)
    if matches_by_country is None:
        raise HTTPException(
            status_code=404, detail=f"Matches for {country} not found")
    return matches_by_country


@router.get("/matches_per_year", response_model=List[schemas.MatchesPerYear])
def read_matches_agg_by_year(db: Session = Depends(get_db)):
    dates = crud.get_match_dates(db)

    # Parse response, aggregate by year, and return in correct format
    date_list = [date for (date,) in dates]
    year_list = [date[:4] for date in date_list]
    year_count_pairs = dict(Counter(year_list))
    year_list_formatted = []
    for key, value in year_count_pairs.items():
        year_list_formatted.append({
            'year': int(key),
            'number_of_matches': int(value)
        })
    return year_list_formatted


@router.get("/matches_played", response_model=List[schemas.MatchesPlayed])
def read_matches_played(limit: int = 100, db: Session = Depends(get_db)):
    all_matches_played = crud.get_all_matches_played(db)

    # Parse response, aggregate by country, and return in correct format
    matches_list = []
    for (home, away) in all_matches_played:
        matches_list.append(home)
        matches_list.append(away)
    team_count_pairs = dict(Counter(matches_list).most_common(limit))
    matches_played_formatted = []
    for key, value in team_count_pairs.items():
        matches_played_formatted.append({
            'country': key,
            'matches_played': int(value)
        })
    return matches_played_formatted

# Example route showing how authentication works


@router.get("/matches_authenticated/", response_model=List[schemas.Match])
def read_matches(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    matches = crud.get_matches(db, skip=skip, limit=limit)
    return matches
