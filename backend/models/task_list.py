from pydantic import BaseModel


class TaskListCreate(BaseModel):
    completo: bool = False
    registro_id: int
