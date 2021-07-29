from backend.controller import tweet
from fastapi import APIRouter

router = APIRouter()

router.include_router(tweet.router)
