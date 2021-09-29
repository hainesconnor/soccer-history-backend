from sqlalchemy.orm import Session

from . import models, schemas
from .. import authentication

# TODO refactor into multiple files organized to match different routers

# Functionality for Users


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = authentication.get_password_hash(user.password)
    db_user = models.User(username=user.username, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# Funcitonality for Matches

def get_matches(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Match).order_by(models.Match.date.desc()).offset(skip).limit(limit).all()


def get_matches_by_country(country: str, db: Session):
    return db.query(models.Match).order_by(models.Match.date.desc()).filter((models.Match.home_team == country) | (models.Match.away_team == country)).all()


def get_match_dates(db: Session):
    return db.query(models.Match.date)


def get_all_matches_played(db: Session):
    return db.query(models.Match.home_team, models.Match.away_team).all()


# Functionality for Countries

def get_countries(db: Session):
    # Assuming everyteam has played at least one home match
    return db.query(models.Match.home_team).distinct().order_by(models.Match.home_team).all()
