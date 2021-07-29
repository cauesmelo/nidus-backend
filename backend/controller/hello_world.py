from fastapi import APIRouter
from pydantic import BaseModel
# import tweepy

router = APIRouter()

class Credentials(BaseModel):
    accessToken: str
    expiresIn: int
    idToken: str
    scope: str
    tokenType: str

class Name(BaseModel):
    name: str

@router.get("/", response_model=str)
def hello():
    return "Hello World!"


@router.get("/teste")
async def teste() -> dict:
    item = {
        "name": "caue",
        "desc": "descricao"
    }
    return item

@router.post("/login")
async def login(name: Name):
    print(name)

