from pathlib import Path

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

# Función que determina que usuarios puede ver el usaurio autenticado según su rol
def get_visible_users(current_user: User) -> list[User]:
    # Obetiene todos los usuarios
    all_users = repo.get_all()

    # Si el usuario es admin puede ver a todos
    if current_user.rol == "admin":
        return all_users

    # Si es supercisor, puede ver supervisores y usuarios
    elif current_user.rol == "supervisor":
        return [u for u in all_users if u.rol in ("supervisor", "usuario")]

    # Si es usuario, solo puede verse a sí mismo
    elif current_user.rol == "usuario":
        return [u for u in all_users if u.username == current_user.username]
    return []