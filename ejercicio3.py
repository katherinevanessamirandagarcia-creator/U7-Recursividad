
def imprimir_patron(n):
    # Caso base: no imprimir si n es menor o igual a cero
    if n <= 0:
        return

    # Caso recursivo: imprimir las filas anteriores
    imprimir_patron(n - 1)

    # Imprimir la fila actual
    print("*" * n)


# Ejemplo de prueba
imprimir_patron(3)
