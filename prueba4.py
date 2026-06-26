listaPeliculas = []
ejecutar = True

def esTituloValido(nombre):
    return nombre.strip() != ""

def esDuracionValida(minutos):
    if minutos.isdigit():
        return int(minutos) > 0
    return False

def esCalificacionValida(nota):
    try:
        nota = float(nota)
        return 0 <= nota <= 10
    except:
        return False

def menu():
    print("=========== CINE ===========")
    print("1.- Agregar película")
    print("2.- Buscar película")
    print("3.- Eliminar película")
    print("4.- Actualizar disponibilidad")
    print("5.- Mostrar películas")
    print("6.- Salir")

def pedirOpcion():
    while True:
        op = input("Ingrese opción: ")

        if op.isdigit():
            op = int(op)

            if op >= 1 and op <= 6:
                return op

        print("Opción incorrecta.")

def registrar(lista):

    nombre = input("Título: ")
    minutos = input("Duración: ")
    nota = input("Calificación: ")

    if not esTituloValido(nombre):
        print("Título inválido.")
        return

    if not esDuracionValida(minutos):
        print("Duración inválida.")
        return

    if not esCalificacionValida(nota):
        print("Calificación inválida.")
        return

    datos = {
        "titulo": nombre,
        "duracion": int(minutos),
        "calificacion": float(nota),
        "disponible": False
    }

    lista.append(datos)

    print("Película registrada correctamente.")

def buscar(lista, nombre):

    contador = 0

    for pelicula in lista:

        if pelicula["titulo"] == nombre:
            return contador

        contador += 1

    return -1

def eliminar(lista):

    nombre = input("Título a eliminar: ")

    lugar = buscar(lista, nombre)

    if lugar == -1:
        print("La película no se encuentra registrada.")
    else:
        del lista[lugar]
        print("Película eliminada.")

def actualizar(lista):

    for pelicula in lista:

        if pelicula["calificacion"] >= 7:
            pelicula["disponible"] = True
        else:
            pelicula["disponible"] = False

def mostrar(lista):

    actualizar(lista)

    print("====== PELÍCULAS ======")

    if len(lista) == 0:
        print("No existen películas.")
        return

    for pelicula in lista:

        print("Título:", pelicula["titulo"])
        print("Duración:", pelicula["duracion"])
        print("Calificación:", pelicula["calificacion"])

        if pelicula["disponible"]:
            print("Estado: DISPONIBLE")
        else:
            print("Estado: NO RECOMENDADA")

        print("-" * 40)

while ejecutar:

    menu()

    opcion = pedirOpcion()

    if opcion == 1:

        registrar(listaPeliculas)

    elif opcion == 2:

        nombre = input("Ingrese título: ")

        posicion = buscar(listaPeliculas, nombre)

        if posicion == -1:
            print("Película no encontrada.")
        else:
            print("Posición:", posicion)
            print(listaPeliculas[posicion])

    elif opcion == 3:

        eliminar(listaPeliculas)

    elif opcion == 4:

        actualizar(listaPeliculas)
        print("Disponibilidad actualizada.")

    elif opcion == 5:

        mostrar(listaPeliculas)

    else:

        print("Gracias por usar el sistema.")
        ejecutar = False

#Prueba de subida con github Maximo

