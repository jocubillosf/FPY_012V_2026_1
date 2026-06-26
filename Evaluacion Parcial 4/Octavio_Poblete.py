#Octavio_Poblete

peliculas = []

def menu(): 
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar película")
    print("2. Buscar película")
    print("3. Eliminar película")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar películas")
    print("6. Salir")
    print("=====================================")

def buscarPelicula(peliculas, titulo):
    for i in range(len(peliculas)):
        if peliculas[i]["titulo"] == titulo:
            return i 
    return -1

def agregar_pelicula(lista_peliculas):

    titulo = input("Ingrese el nombre de la pelicula: ")
    if titulo == "":
        print("Nombre invalido")
        return
    
    duracion = int(input("Ingrese la duracion de la pelicula: "))
    if duracion <= 0:
        print("Duracion invalida")
        return
    
    calificacion = float(input("Ingrese la clasificacion de la pelicula: "))
    if calificacion < 1.0 or calificacion > 10.0:
        print("Calificacion erronea")
        return
    
   
    nueva_pelicula = {
        "titulo": titulo,
        "duracion": duracion,
        "calificacion": calificacion,
        "disponible": False
    }

    lista_peliculas.append(nueva_pelicula)
    print("Pelicula agregada.")

def actualizarDisponibilidad(pelicula):
    for p in pelicula:
        if p["calificacion"] >= 7.0:
            p["disponible"] = True
        else:
            p["disponible"] = False

    print("Calificacion actualizada.")
        
def MostrarPeliculas(pelicula):

    actualizarDisponibilidad(pelicula)

    if len(pelicula) == 0:
        print("No hay peliculas disponibles")
        return 

    print("=== LISTA DE PELICULAS ===")


    for p in pelicula:
        print("Titulo:", p["titulo"])
        print("Duracion:", p["duracion"])
        print("Calificacion:", p["calificacion"])

        if p["disponible"]:
            print("Estado: Disponible")
        else:
            print("Estado: No Recomendada")
        print("*********************************************")


opcion = 0

while opcion != 6:
    menu()
    opcion = int(input("Seleccione una opcion: "))

    if opcion == 1:
        agregar_pelicula(peliculas)
    elif opcion == 2:
        titulo = input("Ingrese el titulo a buscar: ")
        posicion = buscarPelicula(peliculas, titulo)

        if posicion == -1:
            print("Pelicula no encontrada")
        else:
            print("Pelicula encontrada en la posicion: {posicion}")
            
    elif opcion == 3:
        titulo = input("Nombre a eliminar: ")
        posicion = buscarPelicula(peliculas, titulo)
        if posicion == -1:
            print("Pelicula no encontrada")
        else:
            peliculas.pop(posicion)
            print("Pelicula eliminada")
            
    elif opcion == 4:
        actualizarDisponibilidad(peliculas)
    elif opcion == 5:
        MostrarPeliculas(peliculas)
    elif opcion == 6:
        print("Gracias por usar el sistema. Vuelva Pronto")
    else:
        print("Opcion incorrecta.")