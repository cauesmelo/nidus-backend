from backend.models.preferences import PreferencesInsert
from backend.models.users import UserInsert
from backend.repository.base import BaseRepository
from backend.schemas import Preferences, Users
from sqlalchemy import insert


class UserRepository(BaseRepository):
    table = Users

    def create(self, user: UserInsert, preferences: PreferencesInsert) -> UserInsert:
        preferences_id = self.insert(Preferences, preferences.dict())
        return self.insert(
            self.table,
            dict(**user.dict(), preferencias_id=preferences_id),
        )
