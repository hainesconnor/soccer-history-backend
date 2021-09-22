from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import home, matches, users, countries


app = FastAPI()
app.include_router(users.router)
app.include_router(matches.router)
app.include_router(home.router)
app.include_router(countries.router)


# Note: Not a secure CORS config, and has not been tested
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
