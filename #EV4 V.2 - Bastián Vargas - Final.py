#EV4 V.2 - Bastián Vargas - Final

Lista_peliculas = []

def Mostrar_peliculas(Lista_peliculas):
    print("*** PELICULAS ***")
    for pelicula in Lista_peliculas:
        estado = "DISPONIBLE" if pelicula["disponible"] == True else "NO RECOMENDADA" #Lo mismo de la opcion 2
        print("===================")
        print(f"Nombre: {pelicula["titulo"]}")
        print(f"Duración: {pelicula["duracion"]}")
        print(f"Calificación {pelicula["calificacion"]}")
        print(f"Estado: {estado}")
        print("===================")


def Actualizar_disponibilidad(Lista_peliculas):
    for pelicula in Lista_peliculas: #Si la califciación cumple, se acutaliza, sino, no
        if pelicula["calificacion"] >= 7.0:
            pelicula["disponible"] = True
        else:
            pelicula["disponible"] = False


def posicion_pelicula(Lista_peliculas, titulo):
    for i, pelicula in enumerate(Lista_peliculas): #usamos enumrate para que nos de las 2 variables que le pedimos, la posicion y la pelicula
        if pelicula["titulo"] == titulo: #Si la pelicula recorrida coincide con la que buscamos, nos retorna su posición
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
        Lista_peliculas.pop(posicion) #Usamos esta funcion para borrar la pelicula mediante la posicion
        print("Pelicula eliminada con éxito")
    else:
        print("Pelicula no encontrada")

    
def Buscar_pelicula():
    print()
    print("***BUSCAR PELICULA ***")
    print("Ingrese el titulo de la pelicula que desea buscar: ")
    titulo = input(":").upper()

    posicion = posicion_pelicula(Lista_peliculas, titulo) #Usamos la funcion para determinar la posicion de la pelicula en la lista

    if posicion != -1: #Si la posicion es distinta de -1, significa que la pelicula existe y coincice con nuestra busqueda
        pelicula = Lista_peliculas[posicion] #Accedemos a los datos de la pélicula mediante la posición
        estado = "DISPONIBLE" if pelicula["disponible"] == True else "NO RECOMENDADA" #Nos encargamos de este dato se actualice y no salga como True/False
        print("¡Pelicula encontrada!")
        print("==============")
        print(f"Titulo: {pelicula["titulo"]}")
        print(f"Duración: {pelicula["duracion"]}")
        print(f"Calificación {pelicula["calificacion"]}")
        print(f"Estado: {estado}")
        print("==============")
    else:
        print("Pelicula no encontrada")



def Validar_calificacion(calificacion:float):
    if calificacion >= 0.0 and calificacion <= 10.0: #Validamos si cumple las condiciones estipuladas en el word
        return True #Retornamos True si cumple
    else:
        print("Calificación invalida") 
        return False
    
def Validar_duracion(duracion:int):
    if duracion.is_integer:
        if duracion < 0:#Si la duración es mayor a cero min., pasa la validación
            print("Duración invalida, debe ser un numero mayor a cero")
            return False
        else:
            return True #Retornamos true si cumple todo
    else:
        return False #retornamos False si de por si falla el ingreso de un entero, es una doble precaución, ya que el try del menu lo cubre
    
def Validar_titulo(titulo):
    contador_letra = 0
    if titulo == " ": #Si el titulo ingresado es un espacio, no pasa la validación
        print("El titulo no puede estar vacio")
        return False
    else:
        for letra in titulo:
            if letra != " ": #Por cada letra, se aumenta el contador
                contador_letra += 1
        if contador_letra == 0: #En dado caso que el contador sea cero, signifcara que el titulo son solos espacios en blanco
            print("El nombre no pueden ser espacios vacíos")
            return False #retornamos un false en cada validación no pasada
        else:
            return True #Retornamos True si cumple todo

def Agregar_pelicula():
    print()
    print("*** AGREGAR PELICULA ***")
    print("Ingrese el Titulo de la película:")
    titulo = input(":").upper()
    if Validar_titulo(titulo): # Validaciones en caso de cada dato ingresado
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
                Lista_peliculas.append(pelicula) #Ya despues´de que pase todas las validaciones hechas con if, se crea y a se agrega el diccionario a a lista
                print("Pelicula agregada con éxito")


def Leer_opc():
    print()
    print("Ingrese una opción: ")
    opc = int(input(":"))
    if opc < 0:
        print("Opción invalida") 
        return True #Retornamos True en caso de que haya un error, así el bucle sigue
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
                return False #Retornamos False solo si selecciona la opción 6
            case _:
                print("Opción no encontrada")
        return True #Retornamos True en si presiona cualquier opcion

def mostrar_menu():
    Bucle_menu = True #Bucle para el menu principal, seguido de un try y except, para controlar errores
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
            Bucle_menu = Leer_opc() #hacemos que el bucle dependa del ingreso de opciones
        except ValueError:
            print("¡ERROR! La opción ingresada debe ser un numero entero positivo") #Mensaje informando el error


mostrar_menu()