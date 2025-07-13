from pydantic import BaseModel

from app.domain.user import Role

# Esquema para la solicitud del login
class LoginRequest(BaseModel):
    username: str
    password: str

# Esquema para la respuesta del login
class LoginResponse(BaseModel):
    username: str
    rol: Role