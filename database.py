import asyncpg
from typing import AsyncGenerator
from config.settings import settings


class Database:
    def __init__(self):
        self._pool = None

    async def init_pool(self):
        if self._pool is None:
            self._pool = await asyncpg.create_pool(dsn=settings.database_url)

    async def close_pool(self):
        if self._pool:
            await self._pool.close()

    async def get_db(self) -> AsyncGenerator[asyncpg.Connection, None]:
        if self._pool is None:
            raise RuntimeError("Database connection pool is not initialized.")

        async with self._pool.acquire() as connection:
            try:
                yield connection
            finally:
                await connection.close()


db = Database()


def get_db() -> Database:
    return db

