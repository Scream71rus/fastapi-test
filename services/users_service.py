from fastapi import Depends

from repositories.users_repository import UsersRepository, get_users_repository, Record


class UsersService:
    def __init__(self, repository: UsersRepository):
        self._repository = repository

    async def fetch_all_users(self) -> list[Record]:
        return await self._repository.get_all_users()


def get_users_service(repository: UsersRepository = Depends(get_users_repository)) -> UsersService:
    return UsersService(repository)

