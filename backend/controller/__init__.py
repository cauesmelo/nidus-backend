from backend.controller import tweet, user
from fastapi import APIRouter

router = APIRouter()

router.include_router(tweet.router)
router.include_router(user.router)
