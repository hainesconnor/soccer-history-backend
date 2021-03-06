from pydantic import BaseModel
from typing import Optional

# Read Matches


class MatchBase(BaseModel):
    date: str
    home_team: str
    away_team: str
    home_score: str
    away_score: str
    tournament: str
    city: str
    country: str
    neutral: bool


class Match(MatchBase):
    id: int

    class Config:
        orm_mode = True

# Read matches agg by year


class MatchesPerYear(BaseModel):
    year: int
    number_of_matches: int

# Read matches played


class MatchesPlayed(BaseModel):
    country: str
    matches_played: int


# Read and Post Users

class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


# Authentication tokens

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
