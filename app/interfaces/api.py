from uuid import uuid4

from litestar import post, Request, Response
from litestar.response import Response
from app.domain.schemas.auth import LoginRequest, LoginResponse
from app.application.auth_service import authenticate_user

# Diccionario para almacenar las sesiones activas en memoria
sessions = {}

# Endpoint para el login de usuarios
@post("/api/login")
async def login(data: LoginRequest) -> Response:
        # Autentica al usuario con las credenciales proporcionadas
        user = authenticate_user(data.username, data.password)

        # Si las credenciales no son válidas, retorna error 401
        if not user:
            return Response(status_code=401, content={"error": "Credenciales inválidas"})

        # Si es válido, se genera un ID de sesión único
        session_id = str(uuid4())

        # Se guarda la sesión en memoria
        sessions[session_id] = user.model_dump()
        print(f"Generando sesión con ID: {session_id}")

        return Response(
            status_code=200,
            content=LoginResponse(username=user.username, rol=user.rol).dict(),
            headers={"X-Session-ID": session_id}
        )

# Endpoint para cerrar sesión
@post("/api/logout")
async def logout(request: Request) -> Response:
    session_id = request.headers.get("X-Session-ID")

    # Verifica si la sesión existe y la elimina
    if session_id and session_id in sessions:
        del sessions[session_id]
        return Response(status_code=200, content={"Mensaje" : "Sesión cerrada correctamente"})

    # Si no existe o ya se cerro, devuelve error
    return Response(status_code=401, content={"error": "Sesión no válida o ya cerrada"})