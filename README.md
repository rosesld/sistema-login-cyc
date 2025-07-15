
# Sistema Login - Prueba Técnica C&C

Este proyecto es una aplicación web de gestión de usuarios con autenticación y control de acceso por roles. Permite autenticar usuarios y mostrar información personalizada según su rol (admin, supervisor o usuario).

El backend está desarrollado con **Python y Litestar**, y permite elegir entre dos orígenes de datos:
- Un archivo JSON.
- Una base de datos SQLite (por defecto).

## Aplicación desplegada

[https://sistema-login-cyc.netlify.app](https://sistema-login-cyc.netlify.app)

---

## Usuarios para prueba

| Rol       | Username     | Contraseña |
|-----------|-------------|------------|
| Admin     | jhon.doe       | password1   |
| Supervisor| ana.torres | password3     |
| Usuario   | camila.navarro       | password13    |

---

---
## Requisitos

- Python 3.10+
- pip
- (Opcional) SQLite instalado localmente para base de datos

---

## Instalación

1. Clona el repositorio

```bash
git clone https://github.com/rosesld/sistema-login-cyc.git
cd sistema_login_cyc

```
---

## Crea y activa un entorno virtual
```bash
python -m venv venv
```
## Windows
```bash
venv\Scripts\activate
```
## Linux/macOS
```
source venv/bin/activate
```
---

## Instala dependencias

```
pip install -r requirements.txt

```

##  Configuración de la fuente de datos

Abre `config.py` y modifica:

```python
USE_DATABASE = True  # Cambia a False para usar usuarios.json
```

## Ejecutar localmente

1. Asegúrate de tener el entorno virtual activado y las dependencias instaladas.

2. Ejecuta el servidor Litestar con:

```bash
python main.py

```

## Ejecutar pruebas

```
pytest

```

## Frontend del proyecto

Este backend se conecta con un frontend desarrollado con HTML, CSS, JavaScript y jQuery.

Repositorio del frontend: [https://github.com/rosesld/sistema-login-cyc-front.git](https://github.com/rosesld/sistema-login-cyc-front.git)

Aplicación en producción: [https://sistema-login-cyc.netlify.app](https://sistema-login-cyc.netlify.app)


## Notas

- Puedes alternar entre JSON y base de datos fácilmente editando config.py.


- El sistema está desacoplado de la fuente de datos, permitiendo fácil migración o integración futura.
