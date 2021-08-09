from backend.models.register import RegisterCreate
from backend.repository.base import BaseRepository
from backend.schemas import Register


class RegisterRepository(BaseRepository):
    table = Register

    def create(self, register: RegisterCreate) -> int:
        return self.insert(self.table, register.dict())
