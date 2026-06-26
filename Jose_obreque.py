opcion=0
menu=""
listaPeliculas=[]
def menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar película")
    print("2. Buscar película")
    print("3. Eliminar película")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar películas")
    print("6. Salir")
    print("=====================================")


def opcion(opcion):
    while True:
        try:
            opcion=int(input("ingrese una opcion: "))
            if opcion<=0 or opcion>6:
                print("ingrese una opcion valida")
            else:
                print("opcion elegida con exito")
                return opcion
        except:
            print("ingrese una opcion valida")


while True:
    menu()
    hola=opcion(opcion)
    match hola:
        case 1:
            while True:
                try:
                    Nombre=input("ingrese el nombre de la pelicula: ")
                    if Nombre.strip()=="":
                        print("Nombre no debe incluir solo espacios")
                    elif len(Nombre)<4:
                        print("Error: ingrese nombre completo de la pelicula: ")
                    else:
                        print("nombre guardado con exito")
                        
                    while True:
                        try:
                            duracion=int(input("introduzca la duracion de la pelicula: "))
                            if duracion<=0:
                                print("Error: ingrese una duracion valida")
                            else:
                                print("duracion registrada con exito")
                                break
                        except:
                            print("ingrese una duracion valida")

                        
                    while True:
                        try:
                            calificacion=float(input("ingrese la calificacion de la pelicula: "))
                            if calificacion<0.0 or calificacion>10.0:
                                print("Error: ingrese una calificacion valida del 0.0 al 10.0")
                            else:
                                print("calificacion guardada con exito")
                                break
                        except:
                            print("ingrese una calificacion valida del 0.0 al 10.0")

                    break    
                except:
                    print("nombre no debe incluir solo espacios")
        case 2:
            print("hola")
        case 3:
            print("hola")
        case 4:
            print("hola")
        case 5:
            print("hola")
        case 6:
            print("gracias por usar nuestro programa")
            break
