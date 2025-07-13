from pathlib import Path

from app.infrastructure.repositories.user_repository import UserRepository
from app.domain.user import User

# Inicializa el repositorio de usuarios, indicando la ruta del archivo JSON
repo = UserRepository(
    file_path=Path(__file__).parent.parent.parent / "app" / "infrastructure" / "data" / "usuarios.json"
)

# Función par autenticar a un usuario por su username y password
def authenticate_user(username: str, password: str) -> User | None:
    # Busca al usuario por nombre de usuario
    user = repo.get_by_username(username)

    # Verifica si existe el usuario y si la contraseña coincide
    if user and user.password == password:
        return user
    return None