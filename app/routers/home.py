from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def home():
    return "Welcome to the soccer history backend"
