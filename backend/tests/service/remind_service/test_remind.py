from backend.client.sendgrid import SendgridClient
from backend.service.remind import RemindService
from pytest import fixture


@fixture
def remind_service() -> RemindService:
    return RemindService(SendgridClient())


def test_remind_correctly_sends_email(remind_service: RemindService) -> None:
    # Act
    remind_service.remind("some_user")
