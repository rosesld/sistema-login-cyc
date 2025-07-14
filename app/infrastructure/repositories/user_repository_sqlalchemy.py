from sqlalchemy.orm import Session
from app.domain.user import User
from app.infrastructure.models.user_model import UserModel
from app.infrastructure.db import SessionLocal


class SQLUserRepository:
    def __init__(self):
        self.db: Session = SessionLocal()

    def get_all(self) -> list[User]:
        users = self.db.query(UserModel).all()
        return [User(
            id=u.id,
            nombre=u.nombre,
            username=u.username,
            password=u.password,
            rol=u.rol,
            renta_mensual=u.renta_mensual,
        ) for u in users]

    def get_by_username(self, username: str) -> User | None:
        user = self.db.query(UserModel).filter(UserModel.username == username).first()
        if not user:
            return None
        return User(
            id=user.id,
            nombre=user.nombre,
            username=user.username,
            password=user.password,
            rol=user.rol,
            renta_mensual=user.renta_mensual
        )
