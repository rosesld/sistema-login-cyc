from litestar import Litestar
from litestar.middleware.base import DefineMiddleware
from starlette.middleware.cors import CORSMiddleware

from app.interfaces.api import login, logout
from app.interfaces.users import get_users
from app.middleware.exception_middleware import ExceptionMiddleware

app = Litestar(
    route_handlers=[login, get_users, logout],
    middleware=[
        DefineMiddleware(ExceptionMiddleware),
        DefineMiddleware(CORSMiddleware,
                         allow_origins=["*"],
                         allow_methods=["*"],
                         allow_headers=["*"],
                         expose_headers=["X-Session-ID"],
        )
    ]
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
