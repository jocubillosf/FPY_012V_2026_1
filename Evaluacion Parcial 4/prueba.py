op = 0
coleccion_Peliculas =[]

def veiw_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar película")
    print("2. Buscar película")
    print("3. Eliminar película")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar películas")
    print("6. Salir")
    print("=====================================")

def tomar_opcion(op):
    try:
        op = int(input("Seleccione una opcion:"))
        if op >= 1 and op <=6:
            return op
        else:
            print("Opcion no valida.")
    except:
        print("opcion no valida.")

def add_pelicula(list):
    pelicula = {"Titulo":"","Duracion":0,"Calificacion":0.0,"Disponible":None}
    name = ""
    dur = 0
    cal = 0.0
    val_titulo = None
    val_duracion = None
    val_calificacion = None

    try:
        name = input("Ingrese el nombre de la pelicula:")
        dur = int(input("Ingrese la duracion de la pelicula:"))
        cal = float(input("Ingresa la calificacion de la pelicula:"))

        if Titulo_vacio(name) and Solo_espacios(name):
            val_titulo = True
        else:
            if Titulo_vacio(name):
                print("El nombre no puede ser solo espacios")
            else:
                print("El nombre no puede estar vacio")

        if Duracion(dur):
            val_duracion = True
        else:
            print("Ingrese una duracion valida.")
            val_duracion = False
    except:
        print("Ingreso invalido no se agregara a la coleccion.")

def Titulo_vacio(name):
    if name != "":
        return True
    else:
        return False
    
def Solo_espacios(name):
    cont_letras = 0
    for x in name:
        if x != " ":
            cont_letras=+1
    if cont_letras != 0:
        return True
    else:
        return False

def Duracion(duracion):
    if duracion > 0:
        return True
    else:
        return False

#=====================================================================================

while op != 6:

    veiw_menu()
    op = tomar_opcion(op)

    match op:

        case 1:
            add_pelicula(coleccion_Peliculas)
        case 2:
            print("Opcion",op)
        case 3:
            print("Opcion",op)
        case 4:
            print("Opcion",op)
        case 5:
            print("Opcion",op)
        case 6:
            print("saliste")
        case _:
            print("Opcion no es valida.")