from typing import Callable
from starlette.types import Scope, Receive, Send
from litestar.middleware.base import MiddlewareProtocol
from litestar.response import Response
import traceback


class ExceptionMiddleware(MiddlewareProtocol):
    def __init__(self, app: Callable):
        # garda la aplicación para luego llamarla
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        try:
            await self.app(scope, receive, send)
        except Exception as e:
            # Si ocurre un error, captura y formatea el traceback completo
            tb = "".join(traceback.format_exception(e))

            # Imprime elerror y el traceback en consola
            print("Excepción capturada:\n", tb)

            # Crea una respuesta JSON con el mensaje y el traceback
            response = Response(
                content={"detail": str(e), "traceback": tb},
                media_type="application/json",
                status_code=500
            )
            # Envía la respuesta de error al cliente
            await response(scope, receive, send)
