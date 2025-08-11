from fastapi.testclient import TestClient

from main import app
from repositories.users_repository import Record
from services import users_service

class MockService():
    async def fetch_all_users(self) -> list[Record]:
        return [Record(id=1, firstName="")]


app.dependency_overrides[users_service.get_users_service] = MockService
client = TestClient(app)


def test_just_test():
    response = client.get(
        "/users",
    )
    assert response.status_code == 200
