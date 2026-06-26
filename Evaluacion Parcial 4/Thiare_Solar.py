opcion = 0
titulo = 0
duracion = 0
calificacion = 0


def mostrarMenu():
    print("--MENÚ PRINCIPAL--")
    print("1) Agregar pelicula")
    print("2) Buscar pelicula")
    print("3) Eliminar pelicula")
    print("4) Mostrar peliculas")
    print("5) Salir")

def leerOpcion():
    try:
        opcion = int(input("Seleccione una opción"))
        return opcion
    except ValueError:
        return  print("Error debe ingresar una opción valida")
    
def validarTitulo():
    if titulo.strip() == " ":
        return False
    return True

def validarDuracion():
    if duracion > 0:
        return True
    return False

def validarCalificacion():
    if 0.0 <= calificacion <= 10.0:
        return True
    return False

def agregarPelicula():
    titulo = input("Ingrese el titulo de la pelicula: ")

    if not validarTitulo:
        print("Error, el titulo no puede estar vacio. ")
        return
    
    try:
        duracion = int(input("Ingrese la duracion: "))
        if not validarDuracion:
            print("Error, la duracion debe ser un numero entero mayor que cero. ")
            return
        calificacion = float(input("Ingrese la calificación de (0.0 a 10.0): "))
        if not validarCalificacion:
            print("Error, la calificacion debe estar entre 0.0 y 10.0")
            return
    except ValueError:
        print("Error, el tipo de dato ingresado es incorrecto")
        return
    
    nuevaPelicula = {
        "titulo": titulo,
        "duracion": duracion,
        "calificacion": calificacion,
        "disponible": False 
    }
    listaPeliculas.append()
    print("¡Pelicula '{titulo}' agregada con exito!")
    