from backend.models.task_list import TaskListCreate
from backend.repository.base import BaseRepository
from backend.schemas import TaskList


class TaskListRepository(BaseRepository):
    table = TaskList

    def create(self, task_list: TaskListCreate) -> int:
        return self.insert(self.table, task_list.dict())
