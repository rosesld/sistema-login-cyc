from pathlib import Path

import bcrypt

from app.domain.user import User
from app.config.settings import USE_DATABASE

if USE_DATABASE:
    from app.infrastructure.repositories.user_repository_sqlalchemy import SQLUserRepository as Repo
else:
    from app.infrastructure.repositories.user_repository import UserRepository as Repo

# Inicializa el repositorio de usuarios
repo = Repo() if USE_DATABASE else Repo(
    file_path=Path(__file__).parent.parent.parent / "app" / "infrastructure" / "data" / "usuarios.json"
)

# Función par autenticar a un usuario por su username y password
def authenticate_user(username: str, password: str) -> User | None:
    # Busca al usuario por nombre de usuario
    user = repo.get_by_username(username)

    # Verifica si existe el usuario y si la contraseña coincide
    if user and bcrypt.checkpw(password.encode("utf-8"), user.password.encode("utf-8")):
        return user
    return None