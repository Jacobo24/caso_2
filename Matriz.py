class Matriz:
    # Constructor para crear una matriz desde una lista de listas
    def __init__(self, datos):
        self.datos = datos

    # Método para imprimir la matriz
    def imprimir(self):
        for fila in self.datos:
            print(" ".join(map(str, fila)))

    # Método para trasponer la matriz
    def transpuesta(self):
        filas = len(self.datos)
        columnas = len(self.datos[0])
        datos_transpuesta = [[self.datos[j][i] for j in range(filas)] for i in range(columnas)]
        return Matriz(datos_transpuesta)

# Crear la matriz inicial
m = Matriz([[1, 2], [3, 4]])

# Imprimir la matriz original
print("Matriz original:")
m.imprimir()

# Generar la matriz transpuesta y imprimirla
print("\nMatriz transpuesta:")
m_transpuesta = m.transpuesta()
m_transpuesta.imprimir()