from typing import Optional

from pydantic import BaseModel, Field


class TaskCreate(BaseModel):
    texto_tarefa: Optional[str]
    completo: bool = False
    lista_id: int
