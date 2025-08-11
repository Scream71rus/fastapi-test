from contextlib import asynccontextmanager
from typing import Type

from fastapi import FastAPI

from repositories.users_repository import Record, get_users_repository
from routers import main_router
from database import db
from services.users_service import get_users_service, UsersService


@asynccontextmanager
async def lifespan(_: FastAPI):
    await db.init_pool()
    yield
    await db.close_pool()

app = FastAPI(lifespan=lifespan)


app.include_router(main_router)
app.qwe = 1


class MockUserService:
    async def fetch_user(self) -> Record:
        return Record.model_validate({'id': 2, 'name': 'mock service'})


def mock_get_users_service() -> MockUserService:
    return MockUserService()


####################


class MockUserRepository:
    async def get_user(self) -> Record:
        return Record.model_validate({'id': 3, 'name': 'mock repo'})


def mock_get_users_repository() -> MockUserRepository:
    return MockUserRepository()


app.dependency_overrides[get_users_repository] = mock_get_users_repository
