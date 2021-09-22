from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from .db.database import SessionLocal

# DB Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
