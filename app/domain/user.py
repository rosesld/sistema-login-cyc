from pydantic import BaseModel
from typing import Literal

# Tipo restringido: solo permite los valores definidos como posibles roles
Role = Literal["admin", "supervisor", "usuario"]

# modelo de dominio
class User(BaseModel):
    id: int
    nombre: str
    username: str
    password: str
    rol: Role
    renta_mensual: float