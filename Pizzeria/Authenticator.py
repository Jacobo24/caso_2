from Pizzeria.Manager import DataBaseManager

class Authenticator:
    def __init__(self, user_database: DataBaseManager):
        self.user_database = user_database

    def authenticate_user(self, user_id, password):
        print(f"Autenticando usuario {user_id}")
        # Código de autenticación de usuario, consultando la base de datos