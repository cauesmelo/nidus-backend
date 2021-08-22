from backend.models.settings import SettingsInsert
from backend.repository.base import BaseRepository
from backend.schemas import Settings

class SettingsRepository(BaseRepository):
    table = Settings

    def create(self, settings: SettingsInsert) -> str:
        return self.insert(self.table, settings.dict())

    def update_settings(self, settings: SettingsInsert) -> None:
        self.update(self.table, settings.id, settings.dict())