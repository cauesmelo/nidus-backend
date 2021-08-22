from typing import Optional
from pydantic import BaseModel
from uuid import UUID

class UserInsert(BaseModel):
    id: UUID
    tw_id: str
    tw_name: str
    tw_access_token: str
    tw_access_token_verifier: str
    tw_profile_picture: str
    tw_email: str
    settings_id: UUID