from backend.models.session import SessionInsert
from backend.repository.base import BaseRepository
from backend.schemas import Session
from datetime import datetime
from uuid import UUID

class SessionRepository(BaseRepository):
    table = Session

    def create(self, session: SessionInsert) -> UUID:
        return self.insert(self.table, session.dict())

    def end_session(self, session_id: UUID) -> bool:
        return self.update(self.table, session_id, dict(end_at=datetime.utcnow))
