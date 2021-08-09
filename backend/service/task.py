from backend.models.task import TaskCreate
from backend.repository.task import TaskRepository
from fastapi import Depends


class TaskService:
    def __init__(self, task_repository: TaskRepository = Depends()) -> None:
        self.task_repository = task_repository

    def create(self, task: TaskCreate) -> int:
        return self.task_repository.create(task)
