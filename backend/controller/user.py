import tweepy
from backend.models.preferences import PreferencesInsert
from backend.models.users import UserInsert
from backend.repository.user import UserRepository
from fastapi import APIRouter, Depends

router = APIRouter(prefix="/user")


@router.post("/create")
async def create(user: UserInsert, preferences: PreferencesInsert, user_repository: UserRepository = Depends()) -> int:
    return user_repository.create(user, preferences)
