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



#=====================================================================================

while op != 6:

    veiw_menu()
    op = tomar_opcion(op)

    match op:

        case 1:
            print("Opcion",op)
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