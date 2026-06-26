#mattheo cisterna - prueba parcial 4

def validar_titulo():
    titulo = input("Ingrese el título: ")

    while titulo == "":
        print("Título inválido.")
        titulo = input("Ingrese el título: ")

    return titulo


def validar_duracion():
    duracion = int(input("Ingrese la duración: "))

    while duracion <= 0:
        print("Duración inválida.")
        duracion = int(input("Ingrese la duración: "))

    return duracion


def validar_calificacion():
    calificacion = float(input("Ingrese la calificación: "))

    while calificacion < 0 or calificacion > 10:
        print("Calificación inválida.")
        calificacion = float(input("Ingrese la calificación: "))

    return calificacion


#--------FUNCIONES-------

def agregar_pelicula(lista):

    titulo = validar_titulo()
    duracion = validar_duracion()
    calificacion = validar_calificacion()

    pelicula = {}

    pelicula["titulo"] = titulo
    pelicula["duracion"] = duracion
    pelicula["calificacion"] = calificacion
    pelicula["disponible"] = False

    lista.append(pelicula)

    print("Película agregada.")


def buscar_pelicula(lista, titulo):

    for i in range(len(lista)):
        if lista[i]["titulo"] == titulo:
            return i

    return -1


def eliminar_pelicula(lista):

    titulo = input("Ingrese el título: ")

    posicion = buscar_pelicula(lista, titulo)

    if posicion != -1:
        lista.pop(posicion)
        print("Película eliminada.")
    else:
        print("La película", titulo, "no se encuentra registrada.")


def actualizar_disponibilidad(lista):

    for pelicula in lista:

        if pelicula["calificacion"] >= 7:
            pelicula["disponible"] = True
        else:
            pelicula["disponible"] = False

    print("Disponibilidad actualizada.")


def mostrar_peliculas(lista):

    actualizar_disponibilidad(lista)

    print(" --- LISTA DE PELÍCULAS --- ")

    if len(lista) == 0:
        print("No hay películas registradas.")

    else:

        for pelicula in lista:

            print("Título:", pelicula["titulo"])
            print("Duración:", pelicula["duracion"])
            print("Calificación:", pelicula["calificacion"])

            if pelicula["disponible"] == True:
                print("Estado: DISPONIBLE")
            else:
                print("Estado: NO RECOMENDADA")

            print("------------------------")


#-------MENU------

def mostrar_menu():

    print()
    print("----- MENÚ PRINCIPAL -----")
    print("1. Agregar película")
    print("2. Buscar película")
    print("3. Eliminar película")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar películas")
    print("6. Salir")


def leer_opcion():

    opcion = int(input("Ingrese una opción: "))

    while opcion < 1 or opcion > 6:
        print("Opción inválida.")
        opcion = int(input("Ingrese una opción: "))

    return opcion


# ----- PROGRAMA PRINCIPAL -------

peliculas = []

opcion = 0

while opcion != 6:

    mostrar_menu()
    opcion = leer_opcion()

    if opcion == 1:
        agregar_pelicula(peliculas)

    elif opcion == 2:

        titulo = input("Ingrese el título: ")

        posicion = buscar_pelicula(peliculas, titulo)

        if posicion == -1:
            print("Película no encontrada.")
        else:
            print("Posición:", posicion)
            print("Título:", peliculas[posicion]["titulo"])
            print("Duración:", peliculas[posicion]["duracion"])
            print("Calificación:", peliculas[posicion]["calificacion"])
            print("Disponible:", peliculas[posicion]["disponible"])

    elif opcion == 3:
        eliminar_pelicula(peliculas)

    elif opcion == 4:
        actualizar_disponibilidad(peliculas)

    elif opcion == 5:
        mostrar_peliculas(peliculas)

print("Gracias por usar el sistema. Vuelva pronto.")