from fastapi import APIRouter

router = APIRouter(prefix="/settings")


# @router.post("/update")
# async def update(
#     user_id: int, preferences: PreferencesUpdate, preferences_repository: PreferencesRepository = Depends()
# ) -> None:
#     preferences_repository.update_preferences(user_id, preferences)

# @router.get("/")
# async def get(
# user_id: str,
# auth: str,
# settings_repository: SettingsRepository = Depends(),
# session_repository: SessionRepository = Depends()
# ) -> Settings:
#   # print(user_id)
#   print(auth)
#     # if(session_repository.validate(access_token=access_token, 
#     #   user_id=user_id) == False):
#     #   return dict(error="Invalid token provided.")
#     # return settings_repository.get(user_id)

