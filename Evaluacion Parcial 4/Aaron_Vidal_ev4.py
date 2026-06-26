opcion = 0
lista_Pelicula: []

def menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar película")
    print("2. Buscar película")
    print("3. Eliminar película")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar películas")
    print("6. Salir")

def seleccionar_pelicula(opcion):
    try:
        opcion = int(input("seleccione su pelicula"))
        if opcion > 0 and opcion <=6:
            return opcion
        else:
            print("seleccione una opcion que sea valida")
    except:
        print("seleccione una opcion que sea valida")

def registro_pelicula(lista_pelicula):
    pelicula = {"nombre":"","duracion":0,"calificacion":0}
    nombre = ""
    duracion = 0
    clasificacion = 0
    validar_nombre = False
    validar_edad = False
    validar_clasificacion = False

    try:
        nombre = int(input("Ingrese el nombre de su pelicula "))
        duracion = int(input("Ingrese la duracion de su pelicula "))
        clasificacion = int(input("Ingrese la clasificacion de su pelicula"))

        if nombre_vacio(nombre) and espacio_nombre(nombre):
            validar_nombre = True
        if 






