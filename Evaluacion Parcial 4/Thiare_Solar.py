opcion = 0

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
    
