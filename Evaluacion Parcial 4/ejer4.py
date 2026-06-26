
# FUNCIONES DE VALIDACIÓN


def validar_titulo(titulo):
    if titulo.strip() == "":
        return False
    return True


def validar_duracion(duracion):
    try:
        duracion = int(duracion)
        if duracion > 0:
            return True
        return False
    except:
        return False


def validar_calificacion(calificacion):
    try:
        calificacion = float(calificacion)
        if 0 <= calificacion <= 10:
            return True
        return False
    except:
        return False



# MENÚ


def mostrar_menu():
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Agregar película")
    print("2. Buscar película")
    print("3. Eliminar película")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar películas")
    print("6. Salir")
    print("=====================================")


def leer_opcion():
    while True:
        try:
            opcion = int(input("Seleccione una opción: "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Debe ingresar una opción entre 1 y 6.")
        except:
            print("Debe ingresar un número válido.")



# AGREGAR PELÍCULA

def agregar_pelicula(lista):

    titulo = input("Ingrese el título: ")

    if not validar_titulo(titulo):
        print("Error: el título no puede estar vacío.")
        return

    duracion = input("Ingrese la duración en minutos: ")

    if not validar_duracion(duracion):
        print("Error: la duración debe ser un número entero mayor que cero.")
        return

    calificacion = input("Ingrese la calificación: ")

    if not validar_calificacion(calificacion):
        print("Error: la calificación debe estar entre 0.0 y 10.0.")
        return

    pelicula = {
        "titulo": titulo,
        "duracion": int(duracion),
        "calificacion": float(calificacion),
        "disponible": False
    }

    lista.append(pelicula)

    print("Película registrada correctamente.")



# BUSCAR PELÍCULA


def buscar_pelicula(lista, titulo):

    for i in range(len(lista)):
        if lista[i]["titulo"] == titulo:
            return i

    return -1



# ELIMINAR PELÍCULA


def eliminar_pelicula(lista):

    titulo = input("Ingrese el título de la película: ")

    posicion = buscar_pelicula(lista, titulo)

    if posicion != -1:
        lista.pop(posicion)
        print("Película eliminada correctamente.")
    else:
        print(f"La película '{titulo}' no se encuentra registrada.")



# ACTUALIZAR DISPONIBILIDAD


def actualizar_disponibilidad(lista):

    for pelicula in lista:

        if pelicula["calificacion"] >= 7:
            pelicula["disponible"] = True
        else:
            pelicula["disponible"] = False



# MOSTRAR PELÍCULAS


def mostrar_peliculas(lista):

    actualizar_disponibilidad(lista)

    print("\n=== LISTA DE PELÍCULAS ===")

    if len(lista) == 0:
        print("No hay películas registradas.")
        return

    for pelicula in lista:

        print("Título:", pelicula["titulo"])
        print("Duración:", pelicula["duracion"])
        print("Calificación:", pelicula["calificacion"])

        if pelicula["disponible"]:
            print("Estado: DISPONIBLE")
        else:
            print("Estado: NO RECOMENDADA")

        print("*" * 45)
        # ==========================
# PROGRAMA PRINCIPAL
# ==========================

peliculas = []

while True:

    mostrar_menu()

    opcion = leer_opcion()

    if opcion == 1:

        agregar_pelicula(peliculas)

    elif opcion == 2:

        titulo = input("Ingrese el título de la película a buscar: ")

        posicion = buscar_pelicula(peliculas, titulo)

        if posicion != -1:

            actualizar_disponibilidad(peliculas)

            print("\nPelícula encontrada")
            print("Posición:", posicion)
            print("Título:", peliculas[posicion]["titulo"])
            print("Duración:", peliculas[posicion]["duracion"])
            print("Calificación:", peliculas[posicion]["calificacion"])

            if peliculas[posicion]["disponible"]:
                print("Estado: DISPONIBLE")
            else:
                print("Estado: NO RECOMENDADA")

        else:
            print(f"La película '{titulo}' no se encuentra registrada.")

    elif opcion == 3:

        eliminar_pelicula(peliculas)

    elif opcion == 4:

        actualizar_disponibilidad(peliculas)
        print("Disponibilidad actualizada correctamente.")

    elif opcion == 5:

        mostrar_peliculas(peliculas)

    elif opcion == 6:

        print("Gracias por usar el sistema. Vuelva Pronto")
        break