peliculas = []
repetir = True



def validarTitulo(titulo):
    if titulo.strip() != "":
        return True
    return False


def validarDuracion(duracion):
    if duracion.isdigit():
        if int(duracion) > 0:
            return True
    return False


def validarCalificacion(calificacion):
    try:
        nota = float(calificacion)
        if nota >= 0 and nota <= 10:
            return True
    except:
        return False
    return False




def mostrarMenu():
    print("====== MENU ======")
    print("1. Agregar película")
    print("2. Buscar película")
    print("3. Eliminar película")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar películas")
    print("6. Salir")


def leerOpcion():
    opcion = input("Seleccione una opción: ")

    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 6:
        opcion = input("Opción inválida. Ingrese nuevamente: ")

    return int(opcion)



def agregarPelicula(lista):

    titulo = input("Ingrese título: ")
    duracion = input("Ingrese duración: ")
    calificacion = input("Ingrese calificación: ")

    if validarTitulo(titulo):

        if validarDuracion(duracion):

            if validarCalificacion(calificacion):

                pelicula = {
                    "titulo": titulo,
                    "duracion": int(duracion),
                    "calificacion": float(calificacion),
                    "disponible": False
                }

                lista.append(pelicula)
                print("Película agregada correctamente.")

            else:
                print("Calificación inválida.")
        else:
            print("Duración inválida.")
    else:
        print("Título inválido.")


def buscarPelicula(lista, titulo):

    for i in range(len(lista)):
        if lista[i]["titulo"] == titulo:
            return i

    return -1


def eliminarPelicula(lista):

    titulo = input("Ingrese título a eliminar: ")

    posicion = buscarPelicula(lista, titulo)

    if posicion != -1:
        lista.pop(posicion)
        print("Película eliminada.")
    else:
        print("La película no se encuentra registrada.")


def actualizarDisponibilidad(lista):

    for pelicula in lista:

        if pelicula["calificacion"] >= 7:
            pelicula["disponible"] = True
        else:
            pelicula["disponible"] = False

    print("Disponibilidad actualizada.")


def mostrarPeliculas(lista):

    actualizarDisponibilidad(lista)

    print("\n=== LISTA DE PELÍCULAS ===")

    for pelicula in lista:

        print("Título:", pelicula["titulo"])
        print("Duración:", pelicula["duracion"])
        print("Calificación:", pelicula["calificacion"])

        if pelicula["disponible"]:
            print("Estado: DISPONIBLE")
        else:
            print("Estado: NO RECOMENDADA")

        print("********************************")



while repetir:

    mostrarMenu()

    opcion = leerOpcion()

    if opcion == 1:
        agregarPelicula(peliculas)

    elif opcion == 2:

        titulo = input("Ingrese título a buscar: ")

        posicion = buscarPelicula(peliculas, titulo)

        if posicion != -1:
            print(peliculas[posicion])
        else:
            print("Película no encontrada.")

    elif opcion == 3:
        eliminarPelicula(peliculas)

    elif opcion == 4:
        actualizarDisponibilidad(peliculas)

    elif opcion == 5:
        mostrarPeliculas(peliculas)

    elif opcion == 6:
        print("Gracias por usar el sistema. Vuelva pronto.")
        repetir = False