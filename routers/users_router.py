from fastapi import APIRouter, Depends

from repositories.users_repository import Record
from services.users_service import UsersService, get_users_service


router = APIRouter()


@router.get("/")
async def get_users_list(service: UsersService = Depends(get_users_service)) -> list[Record]:
    records = await service.fetch_all_users()
    return records
