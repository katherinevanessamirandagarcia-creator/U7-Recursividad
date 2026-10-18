
def aplanar_lista(lista):
    # Lista donde guardaremos los elementos
    resultado = []

    # Recorrer cada elemento
    for elemento in lista:
        if isinstance(elemento, list):
            # Caso recursivo: aplanar la sublista
            resultado.extend(aplanar_lista(elemento))
        else:
            # Caso base para cada elemento que no sea una lista
            resultado.append(elemento)

    return resultado


# Ejemplo de prueba
datos = [1, [2, [3, 4], 5]]
print(aplanar_lista(datos))
