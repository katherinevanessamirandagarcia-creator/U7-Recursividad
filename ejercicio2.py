
def contar_vocales(texto):
    # Caso base: la cadena está vacía
    if texto == "":
        return 0

    # Comprobar si el primer carácter es vocal
    vocales = "aeiouáéíóú"
    primera = texto[0].lower()

    if primera in vocales:
        cantidad = 1
    else:
        cantidad = 0

    # Caso recursivo: procesar el resto del texto
    return cantidad + contar_vocales(texto[1:])


# Ejemplo de prueba
palabra = "Recursividad"
print("Cantidad de vocales:", contar_vocales(palabra))
