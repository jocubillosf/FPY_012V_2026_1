peliculas=[]
def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1.- Agregar película")
    print("2.- Buscar película")
    print("3.- Eliminar película")
    print("4.- Actualizar disponibilidad")
    print("5.- Mostrar películas")
    print("6.- Salir")
    print("=====================================")
def opcion_elegir():
    while True:
        try:
            opcion=int(input("Seleccione opción: "))
            if opcion < 1 or opcion > 6:
                print("Opción inválida")
            else:
                return opcion
        except:
            print("ingrese número válido")
def buscar_pelicula(peliculas, nombre_buscar):
    for posicion, pelicula in enumerate(peliculas):
        if pelicula["Nombre"].lower() == nombre_buscar.lower():
            return posicion
    return -1

while True:
    mostrar_menu()
    opcion = opcion_elegir()
    if opcion == 1:
        while True:
            titulo = input("Ingrese Título: ")
            if " " in titulo:
                print ("No puede tener espacios ni estar vacío")
            else:
                break
        while True:
            duracion = int(input("Ingrese duración: "))
            if duracion < 0:
                print ("Debe ser un número entero mayor a 0")
            else:
                break
        while True:
            calificacion = float(input("Ingrese calificación: "))
            if calificacion < 0.0 or calificacion > 10.0:
                print("Inválido, debe ser un número entre 0.0 y 10.0")   
            else:
                break
        pelicula= {
            "Nombre": titulo,
            "Duración": duracion,
            "Calificación": calificacion
        }
        
        peliculas.append(pelicula)
    if opcion == 2:
        nombre_buscar = input("Ingrese nombre de película que desea buscar: ")
        posicion = buscar_pelicula(peliculas, nombre_buscar)
        if posicion == -1:
            print("La película 'titulo' no se encuentra registrada.")
            print("=============")

        else:
            pelicula = peliculas[posicion]
            print("Nombre película: ", pelicula["Nombre"])
            print("Duración: ", pelicula["Duración"], " horas")
            print("calificacion: ", pelicula["Calificación"])
            print("=============")

    if opcion == 3:
        nombre_buscar = input("Ingrese nombre de película que desea buscar: ")
        posicion = buscar_pelicula(peliculas, nombre_buscar)
        if posicion == -1:
            print("La película 'titulo' no se encuentra registrada.")
            print("=============")

        else:
            del peliculas[posicion]
            print ("Película eliminada")
            print("=============")

    if opcion == 4:
        for pelicula in peliculas:
            print("Nombre película: ", pelicula["Nombre"])
            print("Duración: ", pelicula["Duración"], " horas")
            if pelicula["Calificación"] >= 7.0:
                print("Estado: Disponible")
                print("=============")
            else:
                print("Estado: NO RECOMENDADA")
            print("=============")
    if opcion == 5:
        for pelicula in peliculas:
            print("Nombre película: ", pelicula["Nombre"])
            print("Duración: ", pelicula["Duración"], " horas")
            print("calificacion: ", pelicula["Calificación"])
            if pelicula["Calificación"] >= 7.0:
                print("Estado: Disponible")
                print("=============")
            else:
                print("Estado: NO RECOMENDADA")
            print("=============")
    if opcion == 6:
        print("Gracias por usar el sistema. Vuelva Pronto")
        break
