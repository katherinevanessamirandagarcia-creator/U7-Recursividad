
def contar_caminos(n, m):
    # Caso base: tablero sin dimensiones válidas
    if n <= 0 or m <= 0:
        return 0

    # Caso base: solo hay una celda
    if n == 1 and m == 1:
        return 1

    # Caso recursivo: venir desde arriba o desde la izquierda
    return contar_caminos(n - 1, m) + contar_caminos(n, m - 1)


# Ejemplo de prueba: tablero de 3 filas y 3 columnas
print("Cantidad de caminos:", contar_caminos(3, 3))
