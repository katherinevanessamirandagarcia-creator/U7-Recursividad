
class ExploradorRecursivo:
    def __init__(self, sistema):
        self.sistema = sistema

    def imprimir_arbol(self, sistema=None, nivel=0):
        # Usar el sistema principal si no se recibe otro diccionario
        if sistema is None:
            sistema = self.sistema

        for nombre, contenido in sistema.items():
            # Mostrar el nombre según el nivel de profundidad
            sangria = "    " * nivel

            if isinstance(contenido, dict):
                # Caso recursivo: es una carpeta
                print(f"{sangria}[CARPETA] {nombre}")
                self.imprimir_arbol(contenido, nivel + 1)
            else:
                # Caso base: es un archivo
                print(f"{sangria}[ARCHIVO] {nombre} ({contenido})")

    def buscar_archivo(self, sistema, nombre, ruta=""):
        # Recorrer todos los elementos del directorio
        for elemento, contenido in sistema.items():
            ruta_actual = f"{ruta}/{elemento}"

            if isinstance(contenido, dict):
                # Caso recursivo: buscar dentro de la carpeta
                resultado = self.buscar_archivo(
                    contenido, nombre, ruta_actual
                )

                if resultado is not None:
                    return resultado
            else:
                # Caso base: encontramos el archivo buscado
                if elemento.lower() == nombre.lower():
                    return ruta_actual

        # Caso base: no se encontró en esta rama
        return None

    def contar_archivos(self, sistema=None):
        # Usar el sistema principal si no se recibe otro diccionario
        if sistema is None:
            sistema = self.sistema

        total = 0

        for contenido in sistema.values():
            if isinstance(contenido, dict):
                # Caso recursivo: contar dentro de la carpeta
                total += self.contar_archivos(contenido)
            else:
                # Caso base: encontramos un archivo
                total += 1

        return total


# Estructura de ejemplo proporcionada por el maestro
sistema_archivos = {
    "Documentos": {
        "apuntes.txt": "10kb",
        "fotos": {
            "vacaciones.png": "2mb",
            "perro.jpg": "1mb"
        }
    },
    "sistema.dll": "500kb"
}


# Crear el explorador
explorador = ExploradorRecursivo(sistema_archivos)

# 1. Mostrar el árbol de directorios
print("=== ARBOL DE DIRECTORIOS ===")
explorador.imprimir_arbol()

# 2. Buscar un archivo
print("\n=== BUSCAR ARCHIVO ===")
nombre_buscado = "perro.jpg"
ruta = explorador.buscar_archivo(
    sistema_archivos, nombre_buscado
)

if ruta is not None:
    print(f"Archivo encontrado: {ruta}")
else:
    print("Archivo no encontrado.")

# 3. Contar los archivos
print("\n=== TOTAL DE ARCHIVOS ===")
print("Cantidad:", explorador.contar_archivos())
