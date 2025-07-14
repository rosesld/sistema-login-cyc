from app.application.auth_service import authenticate_user

# Prueba que un usuario válido con contraseña crrecta pueda autenticarse
def test_auth_valid_user():
    user = authenticate_user("jhon.doe", "password1")

    # Verifica que se devuelve un objeto usuario
    assert user is not None

    # Verifica que el nombre de usuario coincida con el esperado
    assert user.username == "jhon.doe"


# Prueba que la autenticación falla si la contraseña es incorrecta
def test_auth_invalid_user():
    user = authenticate_user("jhon.doe", "password2")

    # Devuelve none por que la contraseña no es válida
    assert user is None

def test_auth_nonexistent_user():
    user = authenticate_user("no.existe", "password1")

    # Usuario que no existe debe devolver None
    assert user is None
