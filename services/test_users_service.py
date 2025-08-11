import pytest
from fastapi import Depends, FastAPI
from fastapi.testclient import TestClient

from main import app
from repositories.users_repository import Record
from repositories.users_repository import get_users_repository
from services import users_service

client = TestClient(app)



class MockRepository():
    async def get_all_users(self) -> list[Record]:
        return [Record(id=1, firstName="")]


app.dependency_overrides[get_users_repository] = MockRepository

@pytest.mark.asyncio
async def test_just_test():
    service = users_service.get_users_service()
    res = await service.fetch_all_users()
    assert res == Record(id=1, firstName="")
