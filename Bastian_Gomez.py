#lista 
peliculas = []

#titulo
def ValidarTitulo(titulo):
    if titulo.strip() !="":
        return True
    else: return False

#Validar dura
def ValidarDuracion(duracion):
    if duracion > 0:
        return True
    else: return False

#Validar Calificacion
def ValidarCalificacion(calificacion):
    if calificacion >= 0 and calificacion <= 10:
        return True
    else:
        return False
    
#Mostrar menu
def MostrarMenu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar película")
    print("2. Buscar película")
    print("3. Eliminar película")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar películas")
    print("6. Salir")
    print("=====================================")

#leer op
def LeerOpcion():
    opcion=int(input("Ingrese una opcion: "))

    while opcion < 1 or opcion > 6:
        opcion = int(input("Error, ingrese una opcion valida: "))
    
    return opcion

#BuscarPelicula
def BuscarPelicula(lista, titulo):
    posicion = -1
    for i in range(len(lista)):
        if lista[i]["titulo"] == titulo:
            posicion = i 
            break
    
    return posicion

#AgregarPelicula
def AgregarPelicula(lista):
    titulo = input("Ingrese el titulo de la pelicula: ")
    duracion = int(input("Ingrese la duracion de la pelicula: "))
    calificacion = float(input("Ingrese la calificacion de la pelicula: "))

    if ValidarTitulo(titulo) == False:
        print("titulo invalido")
        return
    
    if ValidarDuracion(duracion) == False:
        print("duracion invalida")
        return
    
    if ValidarCalificacion(calificacion) == False:
        print("calificacion invalida")
        return
    
    pelicula = {
        "titulo": titulo,
        "duracion": duracion,
        "calificacion": calificacion,
        "disponible": False
    }
    lista.append(pelicula)
    print("Pelicula agregada correctamente")

#eliminar pelicula
def EliminarPelicula(lista):
    titulo = input("Ingrese el titulo de la pelicula: ")
    posicion = BuscarPelicula(lista, titulo)

    if posicion == -1:
        print("La pelicula", titulo, "no se encuentra en la lista")
    else:
        lista.pop(posicion)
        print("Pelicula eliminada correctamente")

#ActualizarDisponibilidad
def ActualizarDisponibilidad(lista):
    
    for i in range(len(lista)):

        if lista[i]["calificacion"] >= 7:
            lista[i]["disponible"] = True
        else:
            lista[i]["disponible"] = False

    print("Disponibilidad actualizada correctamente")

#MostrarPeliculas
def MostrarPeliculas(lista):
    if len(lista) == 0:
        print("No hay peliculas en la lista")
        return
    
    for i in range(len(lista)):
        print("Titulo:", lista[i]["titulo"])
        print("Duracion:", lista[i]["duracion"])
        print("Calificacion:", lista[i]["calificacion"])
        print("Disponible:", lista[i]["disponible"])
        print("-----------------------------")
        
#Programa principal
opcion = 0
while opcion != 6:
    MostrarMenu()
    opcion = LeerOpcion()

    if opcion == 1:
        AgregarPelicula(peliculas)
    elif opcion == 2:
        titulo = input("Ingrese el titulo de la pelicula: ")
        posicion = BuscarPelicula(peliculas, titulo)
        if posicion == -1:
            print("La pelicula", titulo, "no se encuentra en la lista")
        else:
            print("La pelicula", titulo, "se encuentra en la lista")
    elif opcion == 3:
        EliminarPelicula(peliculas)
    elif opcion == 4:
        ActualizarDisponibilidad(peliculas)
    elif opcion == 5:
        MostrarPeliculas(peliculas)

print("Gracias por usar el sistema. Vuelva pronto.")