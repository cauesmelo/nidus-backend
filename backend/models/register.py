from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class RegisterCreate(BaseModel):
    tweet_content: str
    data_hora_registro: Optional[datetime] = Field(default_factory=datetime.utcnow)
    tweet_id: int
    parent_tweet_id: Optional[int]
    usuario_id: int
    tipo_registro: int = 1
