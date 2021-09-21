from typing import List, Optional

from pydantic import BaseModel


# Read and Post Users

class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


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