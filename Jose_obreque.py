lista_peliculas = []

def mostrar_menu():
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
        try:
            opcion = int(input("Ingrese una opción: "))
            if opcion < 1 or opcion > 6:
                print("Ingrese una opción válida (1-6)")
            else:
                return opcion
        except:
            print("Ingrese una opción válida (1-6)")

def validar_titulo(titulo):
    if titulo.strip() == "":
        return False
    return True

def validar_duracion(duracion):
    try:
        duracion = int(duracion)
        if duracion <= 0:
            return False
        return True
    except:
        return False

def validar_calificacion(calificacion):
    try:
        calificacion = float(calificacion)
        if calificacion < 0.0 or calificacion > 10.0:
            return False
        return True
    except:
        return False

def agregar_pelicula(lista):
    titulo = input("Ingrese el título: ")
    if not validar_titulo(titulo):
        print("Error: el título no puede estar vacío.")
        return

    duracion = input("Ingrese la duración (minutos): ")
    if not validar_duracion(duracion):
        print("Error: la duración debe ser un número entero mayor que cero.")
        return

    calificacion = input("Ingrese la calificación (0.0 - 10.0): ")
    if not validar_calificacion(calificacion):
        print("Error: la calificación debe ser entre 0.0 y 10.0.")
        return

    pelicula = {
        "titulo": titulo,
        "duracion": int(duracion),
        "calificacion": float(calificacion),
        "disponible": False
    }
    lista.append(pelicula)
    print("Película agregada con éxito.")

def buscar_pelicula(lista, titulo):
    for i in range(len(lista)):
        if lista[i]["titulo"] == titulo:
            return i
    return -1

def eliminar_pelicula(lista):
    titulo = input("Ingrese el título a eliminar: ")
    pos = buscar_pelicula(lista, titulo)
    if pos != -1:
        lista.pop(pos)
        print("Película eliminada con éxito.")
    else:
        print(f"La película '{titulo}' no se encuentra registrada.")

def actualizar_disponibilidad(lista):
    for pelicula in lista:
        if pelicula["calificacion"] >= 7.0:
            pelicula["disponible"] = True
        else:
            pelicula["disponible"] = False

def mostrar_peliculas(lista):
    actualizar_disponibilidad(lista)
    print("=== LISTA DE PELICULAS ===")
    for pelicula in lista:
        if pelicula["disponible"] == True:
            estado = "DISPONIBLE"
        else:
            estado = "NO RECOMENDADA"
        print("Título:", pelicula["titulo"])
        print("Duración:", pelicula["duracion"])
        print("Calificación:", pelicula["calificacion"])
        print("Estado:", estado)
        print("*" * 45)

while True:
    mostrar_menu()
    opcion = leer_opcion()

    if opcion == 1:
        agregar_pelicula(lista_peliculas)
    elif opcion == 2:
        titulo = input("Ingrese el título a buscar: ")
        pos = buscar_pelicula(lista_peliculas, titulo)
        if pos != -1:
            p = lista_peliculas[pos]
            print("Película encontrada en posición", pos)
            print("Título:", p["titulo"])
            print("Duración:", p["duracion"])
            print("Calificación:", p["calificacion"])
            print("Disponible:", p["disponible"])
        else:
            print(f"La película '{titulo}' no se encuentra registrada.")
    elif opcion == 3:
        eliminar_pelicula(lista_peliculas)
    elif opcion == 4:
        actualizar_disponibilidad(lista_peliculas)
        print("Disponibilidad actualizada.")
    elif opcion == 5:
        mostrar_peliculas(lista_peliculas)
    elif opcion == 6:
        print("Gracias por usar el sistema. Vuelva Pronto")
        break