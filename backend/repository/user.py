from backend.models.user import UserInsert, User
from backend.repository.base import BaseRepository
from backend.schemas import User
from uuid import UUID


class UserRepository(BaseRepository):
    table = User

    def __init__(self) -> None:
        super().__init__()

    def create(self, user: UserInsert) -> UUID:
        return self.insert(
            self.table,
            dict(**user.dict()),
        )

    # TODO: Verify why join is not working
    def find_by_email(self, email: str) -> User:
        return self.session.query(self.table)\
            .join(User.settings)\
            .filter(self.table.tw_email==email).first()

    def find_by_id(self, id: int) -> User:
        return self.session.query(self.table).filter(self.table.id==id).first()