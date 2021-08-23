from backend.controller import user, settings, login
from fastapi import APIRouter

router = APIRouter()

# router.include_router(tweet.router)
router.include_router(user.router)
router.include_router(settings.router)
router.include_router(login.router)
