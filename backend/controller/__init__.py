from fastapi import APIRouter
from backend.controller import hello_world

router = APIRouter()

router.include_router(hello_world.router)
