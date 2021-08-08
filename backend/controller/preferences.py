import tweepy
from backend.models.preferences import PreferencesUpdate
from backend.repository.preferences import PreferencesRepository
from fastapi import APIRouter, Depends

router = APIRouter(prefix="/preferences")


@router.post("/update")
async def update(
    user_id: int, preferences: PreferencesUpdate, preferences_repository: PreferencesRepository = Depends()
) -> None:
    preferences_repository.update_preferences(user_id, preferences)
