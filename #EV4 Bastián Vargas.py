#EV4 Bastián Vargas

Lista_peliculas = []

def Mostrar_peliculas(Lista_peliculas):
    print("*** PELICULAS ***")
    for pelicula in Lista_peliculas:
        estado = "DISPONIBLE" if pelicula["disponible"] == True else "NO RECOMENDADA"
        print("===================")
        print(f"Nombre: {pelicula["titulo"]}")
        print(f"Duración: {pelicula["duracion"]}")
        print(f"Calificación {pelicula["calificacion"]}")
        print(f"Estado: {estado}")
        print("===================")


def Actualizar_disponibilidad(Lista_peliculas):
    for pelicula in Lista_peliculas:
        if pelicula["calificacion"] >= 7.0:
            pelicula["disponible"] = True
        else:
            pelicula["disponible"] = False


def posicion_pelicula(Lista_peliculas, titulo):
    for i, pelicula in enumerate(Lista_peliculas):
        if pelicula["titulo"] == titulo:
            return i
    else:
        return -1

def Eliminar_pelicula():
    print()
    print("*** ELIMINAR PELICULA ***")
    print("Ingrese el titulo de la pelicula que desea eliminar: ")
    titulo = input(":").upper()

    posicion = posicion_pelicula(Lista_peliculas, titulo)

    if posicion != -1:
        Lista_peliculas.pop(posicion)
        print("Pelicula eliminada con éxito")
    else:
        print("Pelicula no encontrada")

    
def Buscar_pelicula():
    print()
    print("***BUSCAR PELICULA ***")
    print("Ingrese el titulo de la pelicula que desea buscar: ")
    titulo = input(":").upper()

    posicion = posicion_pelicula(Lista_peliculas, titulo)

    if posicion != -1:
        pelicula = Lista_peliculas[posicion]
        estado = "DISPONIBLE" if pelicula["disponible"] == True else "NO RECOMENDADA"
        print("Pelicula encontrada")
        print(f" Titulo: {pelicula}")
        print(f"Duración: {pelicula["duracion"]}")
        print(f"Calificación {pelicula["calificacion"]}")
        print(f"Estado: {estado}")
    else:
        print("Pelicula no encontrada")



def Validar_calificacion(calificacion:float):
    if calificacion >= 0.0 and calificacion <= 10.0:
        return True
    else:
        print("Calificación invalida")
        return False
    
def Validar_duracion(duracion:int):
    if duracion.is_integer:
        if duracion < 0:
            print("Duración invalida, debe ser un numero mayor a cero")
            return False
        else:
            return True
    else:
        return False
    
def Validar_titulo(titulo):
    contador_letra = 0
    if titulo == " ":
        print("El titulo no puede estar vacio")
        return False
    else:
        for letra in titulo:
            if letra != " ":
                contador_letra += 1
        if contador_letra == 0:
            print("El nombre no pueden ser espacios vacíos")
            return False
        else:
            return True

def Agregar_pelicula():
    print()
    print("*** AGREGAR PELICULA ***")
    print("Ingrese el Titulo de la película:")
    titulo = input(":").upper()
    if Validar_titulo(titulo):
        print("Ingrese la duracion de la pelicula en minutos: ")
        duracion = int(input(":"))
        if Validar_duracion(duracion):
            print("Ingrese la calificación de la pelicula: ")
            calificacion = float(input(":"))
            if Validar_calificacion(calificacion):
                pelicula = {
                    "titulo": titulo,
                    "duracion": duracion,
                    "calificacion": calificacion,
                    "disponible": False
                }
                Lista_peliculas.append(pelicula)
                print("Pelicula agregada con éxito")


def Leer_opc():
    print()
    print("Ingrese una opción: ")
    opc = int(input(":"))
    if opc < 0:
        print("Opción invalida")
        return True
    else:
        match opc:
            case 1:
                Agregar_pelicula()
            case 2:
                Buscar_pelicula()
            case 3:
                Eliminar_pelicula()
            case 4:
                Actualizar_disponibilidad(Lista_peliculas)
            case 5:
                Mostrar_peliculas(Lista_peliculas)
            case 6:
                print()
                print("Gracias por usar el sistema. Vuelva Pronto")
                return False
            case _:
                print("Opción no encontrada")
        return True

def mostrar_menu():
    Bucle_menu = True
    while Bucle_menu:
        try:
            print("""========== MENÚ PRINCIPAL ==========
1. Agregar película
2. Buscar película
3. Eliminar película
4. Actualizar disponibilidad
5. Mostrar películas
6. Salir
=====================================
""")
            Bucle_menu = Leer_opc()
        except ValueError:
            print("¡ERROR! La opción ingresada debe ser un numero entero positivo")


mostrar_menu()