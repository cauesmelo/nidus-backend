from backend.models.task import TaskCreate
from backend.repository.base import BaseRepository
from backend.schemas import Task


class TaskRepository(BaseRepository):
    table = Task

    def create(self, task: TaskCreate) -> int:
        return self.insert(self.table, task.dict())
