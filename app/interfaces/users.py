from typing import List, Dict, Any

from litestar import get, Request, Response
from app.application.user_service import get_visible_users
from app.domain.user import User
from app.interfaces.api import sessions

# Ruta GET - Devuelve una lista de usuarios visible según el rol del usuario
@get("/api/users")
async def get_users(request: Request) -> List[Dict[str, Any]]:
    # Obtiener el ID de sesión desde encabezado HTTP
    session_id = request.headers.get("X-Session-ID")

    # Verifica si hay una sesión válida
    if not session_id or session_id not in sessions:
        return Response(status_code=401, content={"error": "Sesión no válida"})

    # Obtener datos del usuario desde la sesión
    user_data = sessions[session_id]

    # Se crea instancia del usuario actual usando el mocelo de dominio
    current_user = User(**user_data)

    # Obtener usuarios visibles segun rol del usuario actual
    visible_users = get_visible_users(current_user)

    # Convertir la lista de objetos User a diccionarios y devolverlos
    return [user.model_dump() for user in visible_users]