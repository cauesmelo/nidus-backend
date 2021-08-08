from typing import List

from backend.client.sendgrid import SendgridClient
from fastapi import Depends


class EmailNotSentError(Exception):
    pass


class RemindService:
    def __init__(self, sendgrid_client: SendgridClient = Depends()) -> None:
        self.sendgrid_client = sendgrid_client

    def remind(self, user: str) -> List[str]:
        tasks_to_remind: list = self._get_tasks_to_remind(user)
        if tasks_to_remind:
            self._remind_tasks(user, tasks_to_remind)
        return tasks_to_remind

    def _get_tasks_to_remind(self, user: str) -> List[str]:
        # TODO: Get user uncompleted tasks from database
        return ["some_task"]

    def _remind_tasks(self, user: str, tasks: List[str]) -> None:
        user_email: str = self._get_user_email(user)
        for task in tasks:
            subject: str = "Task reminder!"
            content: str = f"Hello {user},\n\nYou have a task to do!\n\n{task}\n\nHave a nice day!"
            response = self.sendgrid_client.send_email(user_email, subject, content)
            if not 200 <= response.status_code < 300:
                raise EmailNotSentError(f"Error sending email to {user!r}")

    def _get_user_email(self, user: str) -> str:
        # TODO: Get user email from database
        return "nidusapp@protonmail.com"
