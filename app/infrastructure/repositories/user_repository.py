import json
from pathlib import Path
from typing import List, Optional
from app.domain.user import User


class UserRepository:
    def __init__(self, file_path: Path):
        self.file_path = file_path
        self.users = self.load_users()

    """
    carga los usuarios desde el archivo json
    """
    def load_users(self) -> List[User]:
        if not self.file_path.exists():
            return []

        with open(self.file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return [User(**user) for user in data]

    """
    devuelve todos los usuarios
    """
    def get_all(self) -> List[User]:
        return self.users

    """
    Devuelve un usuario que coincida con el username, o None si no existe
    """
    def get_by_username(self, username: str) -> Optional[User]:
        #print(f"Buscando usuario: {username}")
        return next((user for user in self.users if user.username == username), None)
