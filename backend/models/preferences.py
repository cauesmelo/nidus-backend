from typing import Optional

from pydantic import BaseModel


class PreferencesInsert(BaseModel):
    integ_anotacoes: int
    integ_tarefas: int
    integ_lembretes: int
    integ_email: int
    integ_push: int


class PreferencesUpdate(BaseModel):
    integ_anotacoes: Optional[int]
    integ_tarefas: Optional[int]
    integ_lembretes: Optional[int]
    integ_email: Optional[int]
    integ_push: Optional[int]
