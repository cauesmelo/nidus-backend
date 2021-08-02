from datetime import datetime

from pydantic import BaseModel, Field


class UserInsert(BaseModel):
    tw_id: int
    tw_token: str
    tw_handle: str
    apelido_usuario: str
    email: str
    registrado_em: datetime = Field(default_factory=datetime.utcnow)
