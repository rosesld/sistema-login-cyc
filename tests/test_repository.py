from pathlib import Path

from app.infrastructure.repositories.user_repository import UserRepository

# Prueba para verificar que se puede obtener un usuario existente por su username
def test_get_existing_user():
    repo = UserRepository(Path("app/infrastructure/data/usuarios.json"))

    # Intenta buscar un usuario que sí existe
    user = repo.get_by_username("jhon.doe")

    # Verifica que el usuario fue encontrado
    assert user is not None

    # Verifica que el username sea el esperado
    assert user.username == "jhon.doe"

# Prueba para verificar que si el usuario no existe, se retorna None
def test_get_non_existing_user():
    repo = UserRepository(Path("app/infrastructure/data/usuarios.json"))
    user = repo.get_by_username("usuario_inexistente")

    # Verifica que el resultado sea None (usuario no encontrado)
    assert user is None
