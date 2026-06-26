opcion = 0
lista_Pelicula = []

def menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar película")
    print("2. Buscar película")
    print("3. Eliminar película")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar películas")
    print("6. Salir")

def seleccionar_opcion():
    while True:
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion > 0 and opcion <= 6:
                return opcion
            else:
                print("Seleccione una opcion que sea valida")
        except:
            print("Seleccione una opcion que sea valida")

def vacio_nombre(nombre):
    return nombre != ""
def espacio_nombre(nombre):
    return nombre.strip() != ""
def validar_duracion_Pelicula(duracion):
    return duracion > 0
def validar_calificacion_Pelicula(calificacion):
    return calificacion >= 0 and calificacion <= 10

def registro_pelicula(lista_pelicula):

    pelicula = {"titulo": "", "duracion": 0,
                "calificacion": 0.0, "disponible": False}

    validar_nombre = False
    validar_duracion = False
    validar_calificacion = False

    try:
        nombre = input("Ingrese el nombre de su pelicula ")
        duracion = int(input("Ingrese la duracion de su pelicula "))
        calificacion = float(input("Ingrese la calificacion de su pelicula "))

        if vacio_nombre(nombre) and espacio_nombre(nombre):
            validar_nombre = True
        else:
            if vacio_nombre(nombre):
                print("El nombre no puede contener solo espacios en blanco")
            else:
                print("El nombre no puede estar vacio")

        if validar_duracion_Pelicula(duracion):
            validar_duracion = True
        else:
            print("La duracion ingresada no es valida")

        if validar_calificacion_Pelicula(calificacion):
            validar_calificacion = True
        else:
            print("La calificacion ingresada no es valida")

        if validar_nombre and validar_calificacion and validar_duracion:

            pelicula["titulo"] = nombre
            pelicula["duracion"] = duracion
            pelicula["calificacion"] = calificacion

            lista_pelicula.append(pelicula)

            print("Pelicula agregada con exito.")

    except:
        print("No se registro la pelicula")

def buscar_pelicula(lista_pelicula, titulo):

    for i in range(len(lista_pelicula)):
        if lista_pelicula[i]["titulo"] == titulo:
            return i

    return -1

def eliminar_pelicula(lista_pelicula):

    titulo = input("Ingrese el titulo de la pelicula a eliminar: ")

    posicion = buscar_pelicula(lista_pelicula, titulo)

    if posicion != -1:
        lista_pelicula.pop(posicion)
        print("Pelicula eliminada correctamente")
    else:
        print(f"La pelicula '{titulo}' no se encuentra registrada.")


def actualizar_disponibilidad(lista_pelicula):

    for pelicula in lista_pelicula:

        if pelicula["calificacion"] >= 7:
            pelicula["disponible"] = True
        else:
            pelicula["disponible"] = False

    print("Disponibilidad actualizada")

def mostrar_peliculas(lista_pelicula):

    actualizar_disponibilidad(lista_pelicula)

    print("=== LISTA DE PELICULAS ===")

    for pelicula in lista_pelicula:

        print("Titulo:", pelicula["titulo"])
        print("Duracion:", pelicula["duracion"])
        print("Calificacion:", pelicula["calificacion"])

        if pelicula["disponible"]:
            print("Estado: DISPONIBLE")
        else:
            print("Estado: NO RECOMENDADA")

while True:

    menu()
    opcion = seleccionar_opcion()

    if opcion == 1:
        registro_pelicula(lista_Pelicula)

    elif opcion == 2:

        titulo = input("Ingrese el titulo a buscar: ")

        posicion = buscar_pelicula(lista_Pelicula, titulo)

        if posicion != -1:

            print("Posicion:", posicion)
            print(lista_Pelicula[posicion])

        else:
            print("La pelicula no existe")

    elif opcion == 3:
        eliminar_pelicula(lista_Pelicula)

    elif opcion == 4:
        actualizar_disponibilidad(lista_Pelicula)

    elif opcion == 5:
        mostrar_peliculas(lista_Pelicula)

    elif opcion == 6:
        print("Gracias por usar el sistema. Vuelva Pronto")
        break








