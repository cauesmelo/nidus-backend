from backend.models.preferences import PreferencesInsert
from backend.models.users import UserInsert
from backend.repository.base import BaseRepository
from backend.repository.preferences import PreferencesRepository
from backend.schemas import Users


class UserRepository(BaseRepository):
    table = Users

    def __init__(self) -> None:
        self.preferences_repository = PreferencesRepository()
        super().__init__()

    def create(self, user: UserInsert, preferences: PreferencesInsert) -> UserInsert:
        return self.insert(
            self.table,
            dict(**user.dict(), preferencias_id=self.preferences_repository.create(preferences)),
        )
