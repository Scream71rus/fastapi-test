from contextlib import asynccontextmanager

from fastapi import FastAPI
from routers import main_router
from database import db


@asynccontextmanager
async def lifespan(_: FastAPI):
    await db.init_pool()
    yield
    await db.close_pool()

app = FastAPI(lifespan=lifespan)


app.include_router(main_router)
