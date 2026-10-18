
def multiplicacion_rusa(a, b):
    # Caso base: multiplicar por cero da cero
    if b == 0:
        return 0

    # Manejar números negativos
    if b < 0:
        return -multiplicacion_rusa(a, -b)

    # Caso recursivo: sumar a y reducir b
    return a + multiplicacion_rusa(a, b - 1)


# Ejemplo de prueba
resultado = multiplicacion_rusa(5, 3)
print("Resultado:", resultado)
