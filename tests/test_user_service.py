from app.application.user_service import get_visible_users
from app.domain.user import User

# Lista de usuarios de prueba con distintos roles
mock_users = [
    User(id=1, nombre="Admin", username="admin", password="x", rol="admin", renta_mensual=20000),
    User(id=2, nombre="Supervidor", username="sup.visor", password="x", rol="supervisor", renta_mensual=28000),
    User(id=3, nombre="Usuario", username="usuario", password="x", rol="usuario", renta_mensual=20000),
]

# Clase dummy que simula el repositorio real, devolviendo los usuarios mock
class DummyRepo:
    def __init__(self, users):
        self.users = users

    def get_all(self):
        return self.users

#  Test: el admin debe poder ver a todos los usuarios
def test_admin_all(monkeypatch):
    # Reemplaza el repo real en user_service por uno simulado
    monkeypatch.setattr("app.application.user_service.repo", DummyRepo(mock_users))

    admin = mock_users[0]
    result = get_visible_users(admin)

    # El admin debe ver a los 3 usuarios
    assert len(result) == 3

# Test: el supervisor debe ver solo a usuarios y supervisores (no admins)
def test_supervisor_and_user(monkeypatch):
    monkeypatch.setattr("app.application.user_service.repo", DummyRepo(mock_users))
    supervisor = mock_users[1]
    result = get_visible_users(supervisor)

    # Debe ver solo 2 usuarios (supervisor y usuario)
    assert len(result) == 2

    # Asegura que no haya admins en la lista
    assert all(u.rol in ("supervisor", "usuario") for u in result)

# Test: el usuario solo debe poder verse a sí mismo
def test_user_self(monkeypatch):
    monkeypatch.setattr("app.application.user_service.repo", DummyRepo(mock_users))
    user = mock_users[2]
    result = get_visible_users(user)

    # Solo debe ver 1 usuario: él mismo
    assert len(result) == 1
    assert result[0].rol in ("supervisor", "usuario")