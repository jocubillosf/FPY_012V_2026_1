

def validar_titulo(titulo):
    
    return titulo.strip() != ""


def validar_duracion(duracion_texto):
    
    if not duracion_texto.isdigit():
        return False
    return int(duracion_texto) > 0


def validar_calificacion(calificacion_texto):
    
    try:
        calificacion = float(calificacion_texto)
    except ValueError:
        return False
    return 0.0 <= calificacion <= 10.0

def validar_titulo(titulo):
    
    return titulo.strip() != ""


def validar_duracion(duracion_texto):

    if not duracion_texto.isdigit():
        return False
    return int(duracion_texto) > 0


def validar_calificacion(calificacion_texto):
   
    try:
        calificacion = float(calificacion_texto)
    except ValueError:
        return False
    return 0.0 <= calificacion <= 10.0
    
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar película")
    print("2. Buscar película")
    print("3. Eliminar película")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar películas")
    print("6. Salir")
    print("=====================================")

def leer_opcion():
    while True:
        opcion_texto = input("Ingrese una opción (1-6): ")
        if opcion_texto.isdigit() and 1 <= int(opcion_texto) <= 6:
            return int(opcion_texto)
        print("Opción inválida. Debe ingresar un número entre 1 y 6.")

def agregar_pelicula(peliculas):
    titulo = input("Ingrese el título de la película: ")
    if not validar_titulo(titulo):
        print("Error: el título no puede estar vacío ni contener solo espacios.")
        return

    duracion_texto = input("Ingrese la duración en minutos: ")
    if not validar_duracion(duracion_texto):
        print("Error: la duración debe ser un número entero mayor que cero.")
        return

    calificacion_texto = input("Ingrese la calificación (0.0 a 10.0): ")
    if not validar_calificacion(calificacion_texto):
        print("Error: la calificación debe ser un número decimal entre 0.0 y 10.0.")
        return

    pelicula = {
        "titulo": titulo,
        "duracion": int(duracion_texto),
        "calificacion": float(calificacion_texto),
        "disponible": False
    }
    peliculas.append(pelicula)
    print(f"Película '{titulo}' agregada exitosamente.")
    
def buscar_pelicula(peliculas, titulo_buscado):
    for i in range(len(peliculas)):
        if peliculas[i]["titulo"] == titulo_buscado:
            return i
    return -1

def opcion_buscar(peliculas):
    titulo = input("Ingrese el título de la película a buscar: ")
    posicion = buscar_pelicula(peliculas, titulo)

    if posicion != -1:
        pelicula = peliculas[posicion]
        print(f"\nPelícula encontrada en la posición {posicion}:")
        print(f"Título: {pelicula['titulo']}")
        print(f"Duración: {pelicula['duracion']}")
        print(f"Calificación: {pelicula['calificacion']}")
        estado = "DISPONIBLE" if pelicula["disponible"] else "NO RECOMENDADA"
        print(f"Estado: {estado}")
    else:
        print(f"La película '{titulo}' no se encuentra registrada.")

def opcion_eliminar(peliculas):
    titulo = input("Ingrese el título de la película a eliminar: ")
    posicion = buscar_pelicula(peliculas, titulo)

    if posicion != -1:
        peliculas.pop(posicion)
        print(f"Película '{titulo}' eliminada exitosamente.")
    else:
        print(f"La película '{titulo}' no se encuentra registrada.")

def actualizar_disponibilidad(peliculas):
    for pelicula in peliculas:
        if pelicula["calificacion"] >= 7.0:
            pelicula["disponible"] = True
        else:
            pelicula["disponible"] = False



def mostrar_peliculas(peliculas):
    actualizar_disponibilidad(peliculas)

    print("\n=== LISTA DE PELICULAS ===")
    if not peliculas:
        print("No hay películas registradas.")
        return

    for pelicula in peliculas:
        print(f"\nTítulo: {pelicula['titulo']}")
        print(f"Duración: {pelicula['duracion']}")
        print(f"Calificación: {pelicula['calificacion']}")
        estado = "DISPONIBLE" if pelicula["disponible"] else "NO RECOMENDADA"
        print(f"Estado: {estado}")
        print("*" * 45)


def main():
    peliculas = []  # Colección general de películas (lista de diccionarios)

    while True:
        mostrar_menu:()
        opcion = leer_opcion()

        if opcion == 1:
            agregar_pelicula(peliculas)
        elif opcion == 2:
            opcion_buscar(peliculas)
        elif opcion == 3:
            opcion_eliminar(peliculas)
        elif opcion == 4:
            actualizar_disponibilidad(peliculas)
            print("Disponibilidad actualizada para todas las películas.")
        elif opcion == 5:
            mostrar_peliculas(peliculas)
        elif opcion == 6:
            print("Gracias por usar el sistema. Vuelva Pronto")
            break


if __name__ == "__main__":
    main()

