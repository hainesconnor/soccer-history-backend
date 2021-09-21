import pandas as pd

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base, engine

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

# Quick hack to setup the database
Base.metadata.create_all(bind=engine)
file_name = "app\db\matches.csv"
df = pd.read_csv(file_name)
df.to_sql(con=engine, index_label='id', name=Match.__tablename__, if_exists='replace')