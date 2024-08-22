from typing import Optional
from fastapi import Depends

from pydantic import BaseModel

from database import Database, get_db


class Record(BaseModel):
    id: int
    firstName: Optional[str]


class UsersRepository:
    def __init__(self, db: Database):
        self._db = db

    async def get_all_users(self) -> list[Record]:
        async for connection in self._db.get_db():
            res = await connection.fetch("SELECT id, \"firstName\" from core.\"User\"")
            return [Record(**i) for i in res]


def get_users_repository(db: Database = Depends(get_db)) -> UsersRepository:
    return UsersRepository(db)
