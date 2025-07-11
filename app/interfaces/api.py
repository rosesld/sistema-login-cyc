from litestar import get, post
from litestar.router import Router

@get("/")
async def home() -> dict:
    return {"mensaje": "prueba"}

routes = [home]