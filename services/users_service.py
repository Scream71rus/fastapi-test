from fastapi import Depends

from repositories.users_repository import UsersRepository, Record, get_users_repository


class UsersService:
    def __init__(self, repository: UsersRepository):
        self._repository = repository

    async def fetch_user(self) -> Record:
        print('run await self._repository.get_user()')
        data = await self._repository.get_user()
        print(data)
        return data


def get_users_service(repository: UsersRepository = Depends(get_users_repository)) -> UsersService:
    return UsersService(repository)

