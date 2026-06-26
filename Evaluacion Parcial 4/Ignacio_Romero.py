peliculas = [

]


def validaTitulo(titulo):
    if titulo.strip() == '':
        return False
    else:
        return True

def validarDuracion(duracion):
        if duracion > 0:
         return True
        else:
            return False
    
def validarCalificacion(calificacion):
    if calificacion >= 0.0 and calificacion <= 10.0:
        return True
    else:
        return False

def agregarPeliculas(lista):

    titulo = input("Ingrese el título de la película: ")
    try:
        duracion = int(input("Ingrese la duración (en minutos): "))
        calificacion = float(input("Ingrese la calificación (0.0 a 10.0): "))
    except ValueError:
        print("Error: La duración y calificación deben ser ingresadas como números")
        return

    if validaTitulo(titulo) == False:
        print("El titulo no puede estar vacio")
    elif validarDuracion(duracion) == False:
        print("Debe ingresar un numero mayor a 0")
    elif validarCalificacion(calificacion) == False:
        print("Debe ingresar una calificacion entre 0 a 10")
    else:
        nueva_Pelicula = {
            "titulo": titulo,
            "duracion": duracion,
            "calificacion": calificacion,
            "disponible": False
        }
        lista.append(nueva_Pelicula)
        print("¡Pelicula agregada con éxito!")

def buscarPelicula(lista, tituloBuscado):
    for i in range(len(lista)):
        if lista [i]["titulo"].lower() == tituloBuscado.lower():
            return i
    return -1

def actualizarDisponibilidad(lista):
    for i in range(len(lista)):
        if lista[i]["calificacion"] >= 7.0:
            lista[i]["disponible"] = True
        else:
            lista[i]["disponible"] = False

def mostrarPeliculas(lista):
    if len(lista) == 0:
        print("No hay películas registradas en el sistema actualmente.")
    else:
        for i in range(len(lista)):
            peliculaActual = lista[i]

            print(f"Título: {peliculaActual['titulo']}")
            print(f"Duración: {peliculaActual['duracion']}")
            print(f"Calificación: {peliculaActual['calificacion']}")
            
            if peliculaActual['disponible'] == True:
                print("Estado: DISPONIBLE")
            else:
                print("Estado: NO RECOMENDADA")
            print("********************************************") 



def MostrarMenu():

    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar Pelicula")
    print("2. Buscar Pelicula")
    print("3. Eliminar Pelicula")
    print("4. Actualizar Disponibilidad")
    print("5. Mostrar Peliculas")
    print("6. Salir")
    print("=====================================")


def ingresarOpcion():
    opcion = 0
    try:
        opcion=int(input("Ingrese una opcion: "))
        if opcion >=1 and opcion <= 6:
            return opcion
        else:
            print("Elije un numero del 1 al 6")
            return 0
    except ValueError:
            print("Debe ingresar un numero entero")
            return 0


while True:

    MostrarMenu()

    opcion = ingresarOpcion()
   
    if opcion == 1:
        agregarPeliculas(peliculas)

    elif opcion == 2:
        print("===== Buscar Pelicula =====")
        tituloBuscar = input("Ingrese el titulo que desea buscar: ")
        posicion = buscarPelicula(peliculas, tituloBuscar)
        
        if posicion != -1:
            print("¡Pelicula Encontrada!")
            print(f"Posición en el sistema: {posicion}") 
            
            pelicula_encontrada = peliculas[posicion]
            print(f"Título: {pelicula_encontrada['titulo']}")
            print(f"Duración: {pelicula_encontrada['duracion']}")
            print(f"Calificación: {pelicula_encontrada['calificacion']}")
            
            if pelicula_encontrada['disponible'] == True:
                print("Estado: DISPONIBLE")
            else:
                print("Estado: NO RECOMENDADA")
        else:
            print(f"La pelicula '{tituloBuscar}' no se encuentra registrada")
        print("")
    elif opcion == 3:
        print("===== Eliminar Pelicula =====")
        tituloEliminar = input("Que pelicula deseas eliminar: ")
        posicion = buscarPelicula(peliculas, tituloEliminar)
        if posicion != -1:
            peliculas.pop(posicion)
            print(f"La pelicula '{tituloEliminar}' ha sido eliminada")
        else:
            print(f"La película '{tituloEliminar}' no se encuentra registrada.")
        print("")

    elif opcion == 4:
        print("===== Actualizar Disponibilidad =====")
        actualizarDisponibilidad(peliculas)
        print("¡La disponibilidad de todas las películas ha sido actualizada!")
        print("")


    elif opcion == 5:
        print("===== Lista de Peliculas =====")
        actualizarDisponibilidad(peliculas)
        mostrarPeliculas(peliculas)
        print("=================================")
    
    elif opcion == 6:
        print("Gracias por usar el sistema. Vuelva Pronto")
        break

