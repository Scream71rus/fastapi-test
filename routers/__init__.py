from fastapi import APIRouter

from .users_router import router as users_router

main_router = APIRouter()

main_router.include_router(users_router, prefix="/users", tags=["users"])


@main_router.get("/")
async def index():
    return {"message": "404"}
