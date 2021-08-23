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

    def validate(self, access_token: UUID, user_id: UUID) -> bool:
        token = self.session.query(self.table)\
            .filter(self.table.access_token==access_token).first()

        if(token != None and token.user_id == user_id and token.active == True):
            return True
        
        return False
