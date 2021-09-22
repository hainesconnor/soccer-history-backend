# from app.dependencies import get_db
# from app.db.crud import get_user_by_username, create_user
# from app.db.schemas import UserCreate, Match
# from app.db.database import Base, engine


# def init_user():
#     # Quick hack to condition a default user
#     db = get_db()
#     user = get_user_by_username(db, username="default_user")
#     if not user:
#         new_user = UserCreate(
#             username = "deafult_user",
#             password = "123"
#         )
#         create_user(db, new_user)

# if __name__=="__main__":
#     init_user()