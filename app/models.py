from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)


class Match(Base):
    __tablename__ = "matches"
   
    id = Column(Integer, primary_key=True, index=True)
    date = Column(String)
    home_team = Column(String)
    away_team = Column(String)
    home_score = Column(Integer)
    away_score = Column(Integer)
    tournament = Column(String)
    city = Column(String)
    country = Column(String)
    neutral = Column(Boolean)

