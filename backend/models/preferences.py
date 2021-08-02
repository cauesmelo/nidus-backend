from pydantic import BaseModel


class PreferencesInsert(BaseModel):
    integ_anotacoes: int
    integ_tarefas: int
    integ_lembretes: int
    integ_email: int
    integ_push: int
