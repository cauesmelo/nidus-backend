from backend.repository.session import SessionRepository
from backend.models.notes import NoteModel, NoteInsert
from backend.repository.notes import NotesRepository
from backend.repository.user import UserRepository
from fastapi import APIRouter, Depends, Header, Request
from uuid import uuid4
import tweepy
import os

API_KEY = os.getenv('API_KEY')
API_SECRET_KEY = os.getenv('API_SECRET_KEY')

router = APIRouter(prefix="/notes")

@router.post("/")
async def post(
    note_insert: NoteInsert,
    authorization: str = Header(None),
    user_id: str = Header(None, convert_underscores=False), 
    notes_repository: NotesRepository = Depends(),
    session_repository: SessionRepository = Depends(),
    user_repository: UserRepository = Depends()
) -> NoteModel:
    if(not(session_repository.validate(authorization, user_id))):
      return dict(error="Invalid token.")

    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    access_token, verifier = user_repository.get_credentials(user_id)
    auth.set_access_token(access_token, verifier)

    api = tweepy.API(auth)

    status = api.update_status(note_insert.content)

    return notes_repository.create(NoteModel(
      id=uuid4(),
      tweet_id= getattr(status, 'id_str'),
      user_id=user_id,
      content=note_insert.content,
    ))


# @router.get("/")
# async def get(user_id: str,
# authorization: str = Header(None),
# settings_repository: SettingsRepository = Depends(),
# session_repository: SessionRepository = Depends()
# ):
#     if(session_repository.validate(authorization, user_id)):
#         return settings_repository.find_by_user_id(user_id)
#     return dict(error="Invalid token.")
