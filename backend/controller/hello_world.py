from fastapi import APIRouter


router = APIRouter(prefix="/hello")

@router.get("/hello", response_model=str)
def hello() -> str:
    return "Hello World!"
