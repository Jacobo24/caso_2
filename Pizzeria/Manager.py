class DataBaseManager:
    def __init__(self, connection_string):
        self.connection_string = connection_string
    
    def connect(self):
        print(f"Conectando a la base de datos con: {self.connection_string}")
        # Código de conexión a la base de datos

    def execute_query(self, query):
        print(f"Ejecutando consulta: {query}")
        # Lógica para ejecutar una consulta