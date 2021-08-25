from uuid import UUID
from pydantic import BaseModel

class NoteModel(BaseModel):
    id: UUID
    tweet_id: str
    user_id: str
    content: str

class NoteInsert(BaseModel):
    content: str
