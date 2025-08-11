import json
from typing import Optional
from fastapi import Depends

from pydantic import BaseModel

from database import Database, get_db


class Record(BaseModel):
    id: int
    name: Optional[str]


class UsersRepository:
    def __init__(self, db: Database):
        self._db = db

    async def get_user(self) -> Record:
        async for connection in self._db.get_db():
            res = await connection.fetch("SELECT json_build_object('id', 1, 'name', 'qwe') AS result")
            data = json.loads(res[0][0])
            return Record.model_validate(data)


def get_users_repository(db: Database = Depends(get_db)) -> UsersRepository:
    return UsersRepository(db)
