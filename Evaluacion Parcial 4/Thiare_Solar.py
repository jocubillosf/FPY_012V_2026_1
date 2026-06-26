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

