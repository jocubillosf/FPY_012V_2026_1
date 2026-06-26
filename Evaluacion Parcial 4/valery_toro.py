def mostrar_menu():
    "Muestra el menú principal"
    print(" MENÚ PRINCIPAL ")
    print("1. Agregar película")
    print("2. Buscar película")
    print("3. Eliminar película")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar películas")
    print("6. Salir")

def leer_opcion():
    "Lee y valida la opción elegida por el usuario"
    while True:
        try:
            opcion = int(input("Seleccione una opción: "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Por favor, elija una opción válida (1-6).")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

def validar_titulo(titulo):
    "Valida que el título no esté vacío ni tenga solo espacios"
    return titulo.strip() != ""

def validar_duracion(duracion):
    "Valida que la duración sea un entero mayor que 0"
    try:
        duracion = int(duracion)
        return duracion > 0
    except ValueError:
        return False

def validar_calificacion(calificacion):
    "Valida que la calificación sea un número entre 0.0 y 10.0."
    try:
        calificacion = float(calificacion)
        return 0.0 <= calificacion <= 10.0
    except ValueError:
        return False

def agregar_pelicula(lista_peliculas):
    "Agrega una nueva película a la lista"
    titulo = input("Ingrese el título de la película: ").strip()
    if not validar_titulo(titulo):
        print("Error: El título no puede estar vacío")
        return

    duracion = input("Ingrese la duración (en minutos): ").strip()
    if not validar_duracion(duracion):
        print("Error: La duración debe ser un número entero mayor que 0.")
        return

    calificacion = input("Ingrese la calificación (0.0 - 10.0): ").strip()
    if not validar_calificacion(calificacion):
        print("Error: La calificación debe ser un número entre 0.0 y 10.0.")
        return

    pelicula = {
        "titulo": titulo,
        "duracion": int(duracion),
        "calificacion": float(calificacion),
        "disponible": False
    }
    lista_peliculas.append(pelicula)
    print(f"La película '{titulo}' ha sido agregada exitosamente.")

def buscar_pelicula(lista_peliculas, titulo):
    "Busca una película por título y retorna su índice o -1 si no existe"
    for i, pelicula in enumerate(lista_peliculas):
        if pelicula["titulo"].lower() == titulo.lower():
            return i
    return -1

def eliminar_pelicula(lista_peliculas):
    "Elimina una película de la lista"
    titulo = input("Ingrese el título de la película a eliminar: ").strip()
    indice = buscar_pelicula(lista_peliculas, titulo)
    if indice != -1:
        lista_peliculas.pop(indice)
        print(f"La película '{titulo}' ha sido eliminada.")
    else:
        print(f"La película '{titulo}' no se encuentra registrada")

def actualizar_disponibilidad(lista_peliculas):
    "Actualiza la disponibilidad de las películas según su calificación"
    for pelicula in lista_peliculas:
        pelicula["disponible"] = pelicula["calificacion"] >= 7.0
    print("La disponibilidad de las películas ha sido actualizada")

def mostrar_peliculas(lista_peliculas):
    "Muestra todas las películas en la lista"
    actualizar_disponibilidad(lista_peliculas)
    print("LISTA DE PELÍCULAS ")
    for pelicula in lista_peliculas:
        estado = "DISPONIBLE" if pelicula["disponible"] else "NO RECOMENDADA"
        print(f"Título: {pelicula['titulo']}")
        print(f"Duración: {pelicula['duracion']} minutos")
        print(f"Calificación: {pelicula['calificacion']}")
        print(f"Estado: {estado}")
    if not lista_peliculas:
        print("No hay películas registradas")

def main():
    "Función principal del programa"
    lista_peliculas = []
    while True:
        mostrar_menu()
        opcion = leer_opcion()
        if opcion == 1:
            agregar_pelicula(lista_peliculas)
        elif opcion == 2:
            titulo = input("Ingrese el título de la película a buscar: ").strip()
            indice = buscar_pelicula(lista_peliculas, titulo)
            if indice != -1:
                pelicula = lista_peliculas[indice]
                print(f"Película encontrada en la posición {indice}:")
                print(f"Título: {pelicula['titulo']}")
                print(f"Duración: {pelicula['duracion']} minutos")
                print(f"Calificación: {pelicula['calificacion']}")
                print(f"Disponible: {'Sí' if pelicula['disponible'] else 'No'}")
            else:
                print("La película '{titulo}' no se encuentra registrada.")
        elif opcion == 3:
            eliminar_pelicula(lista_peliculas)
        elif opcion == 4:
            actualizar_disponibilidad(lista_peliculas)
        elif opcion == 5:
            mostrar_peliculas(lista_peliculas)
        elif opcion == 6:
            print("Gracias por usar el sistema. Vuelva pronto.")
            break

if __name__ == "__main__":
    main()