from .db.database import SessionLocal

# DB Session


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
