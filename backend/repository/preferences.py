from backend.models.preferences import PreferencesInsert, PreferencesUpdate
from backend.repository.base import BaseRepository
from backend.schemas import Preferences


class PreferencesRepository(BaseRepository):
    table = Preferences

    def create(self, preferences: PreferencesInsert) -> int:
        return self.insert(self.table, preferences.dict())

    def update_preferences(self, user_id: int, preferences: PreferencesUpdate) -> None:
        self.update(self.table, self._get_preferences_id_by_user(user_id), preferences.dict())

    def _get_preferences_id_by_user(self, user_id: int) -> int:
        return self.table.select().where(self.table.c.usuario_id == user_id).execute().fetchone()[0]
