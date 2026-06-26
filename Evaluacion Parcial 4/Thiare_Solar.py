

def mostrarMenu():
    print("--MENÚ PRINCIPAL--")
    print("1) Agregar pelicula")
    print("2) Buscar pelicula")
    print("3) Eliminar pelicula")
    print("4) actualizar pelicula")
    print("5) Mostrar peliculas")
    print("6) Salir")

def leerOpcion():
    try:
        opcion = int(input("Seleccione una opción: "))
        return opcion
    except ValueError:
        return  print("Error debe ingresar una opción valida")
    
def validarTitulo(titulo):
    if titulo.strip() == " ":
        return False
    return True

def validarDuracion(duracion):
    if duracion > 0:
        return True
    return False

def validarCalificacion(calificacion):
    if 0.0 <= calificacion <= 10.0:
        return True
    return False

def agregarPelicula(listaPeliculas):
    titulo = input("Ingrese el titulo de la pelicula: ")

    if not validarTitulo(titulo):
        print("Error, el titulo no puede estar vacio. ")
        return
    
    try:
        duracion = int(input("Ingrese la duracion: "))
        if not validarDuracion(duracion):
            print("Error, la duracion debe ser un numero entero mayor que cero. ")
            return
        calificacion = float(input("Ingrese la calificación de (0.0 a 10.0): "))
        if not validarCalificacion(calificacion):
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
    listaPeliculas.append(nuevaPelicula)
    print(f"¡Pelicula '{titulo}' agregada con exito!")

def buscarPelicula(listaPeliculas, tituloBuscar):
    for i in range(len(listaPeliculas)):
        if listaPeliculas [i]["titulo"] == tituloBuscar:
            return i 
    return -1

def eliminarPelicula(listaPeliculas):
    tituloEliminar = input("Ingrese el titulo de la pelicula a eliminar: ")
    posicion = buscarPelicula

    if posicion != -1:
        listaPeliculas.pop(posicion)
        print(f"La pelicula '{tituloEliminar}' fue eliminada correctamente. ")
    else:
        print(f"La pelicula '{tituloEliminar}' no se encuentra registrada. ")

def actualizarDisponibilidad(listaPeliculas):
    
    for pelicula in listaPeliculas:
        if pelicula["calificacion"] >= 7.0:
            pelicula["disponible"] = True
        else:
            pelicula["disponible"] = False


def mostrarPeliculas(listaPeliculas):
    
    actualizarDisponibilidad(listaPeliculas)
    
    if len(listaPeliculas) == 0:
        print("No hay películas registradas en el sistema.")
        return

    print("LISTA DE PELICULAS")
    for pelicula in listaPeliculas:
        print(f"Título: {pelicula['titulo']}")
        print(f"Duración: {pelicula['duracion']}")
        print(f"Calificación: {pelicula['calificacion']}")
        
        if pelicula["disponible"]:
            print("Estado: DISPONIBLE")
        else:
            print("Estado: NO RECOMENDADA")
        print("*" * 44)




def main():
    coleccionPeliculas = []
    
    while True:
        mostrarMenu()
        opcion = leerOpcion()

        if opcion == 1:
            agregarPelicula(coleccionPeliculas)
        elif opcion == 2:
            titulo_b = input("Ingrese el título de la película a buscar: ")
            pos = buscarPelicula(coleccionPeliculas, titulo_b)
            if pos != -1:
                peli = coleccionPeliculas[pos]
                print(f"Película encontrada en la posición {pos}:")
                print(f"Título: {peli['titulo']} | Duración: {peli['duracion']} min | Calificación: {peli['calificacion']}")
            else:
                print("Película no encontrada.")
        elif opcion == 3:
            eliminarPelicula(coleccionPeliculas)
        elif opcion == 4:
            actualizarDisponibilidad(coleccionPeliculas)
            print("Disponibilidad de todas las películas actualizada con éxito.")
        elif opcion == 5:
            mostrarPeliculas(coleccionPeliculas)
        elif opcion == 6:
            print("“Gracias por usar el sistema. Vuelva Pronto”")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()            
