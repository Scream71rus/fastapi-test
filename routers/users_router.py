import os
from typing import Annotated, Union

from fastapi import APIRouter, Depends, Request, Header, Body, Query
import asyncio

from repositories.users_repository import Record
from services.users_service import UsersService, get_users_service
from pydantic import BaseModel, Field

router = APIRouter()


class TestBody(BaseModel):
    qwe: str
    number: int


class PaginationParams(BaseModel):
    lim: str | int
    off: int


# @router.get("/")
# async def get_users_list(
#         request: Request,
#         a: Annotated[PaginationParams, Query()],
#         # b: Annotated[TestBody, Body()]
# ) -> PaginationParams:
#     print(a.lim)
#     return PaginationParams.model_validate({'lim': 1, 'off': 1})
#

@router.get("/")
async def get_users_list(service: UsersService = Depends(get_users_service)) -> Record:
    # print(request.app.dependency_overrides)
    # r = os.urandom(4).hex()
    # print(f'now - {request.app.qwe}. will be set - {r}')
    # request.app.qwe = r
    # await asyncio.sleep(10)

    records = await service.fetch_user()
    return records
