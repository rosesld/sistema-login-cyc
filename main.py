from litestar import Litestar
from app.interfaces.api import routes

app = Litestar(route_handlers=routes)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)