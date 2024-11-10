# auth.py
import json

# Usuarios de ejemplo (en un sistema real, esto debería estar en una base de datos)
USERS = {
    "admin": "password123",
    "user1": "mypassword"
}

def authenticate(username, password):
    """Verifica si las credenciales son correctas."""
    if username in USERS and USERS[username] == password:
        return True
    return False

def login_response(success):
    """Devuelve una respuesta JSON para el login."""
    if success:
        return json.dumps({"status": "success", "message": "Inicio de sesión exitoso"})
    else:
        return json.dumps({"status": "error", "message": "Credenciales inválidas"})
