#Prueba4Hector
def validar_titulo(titulo):
    return titulo.strip() != " "

def validar_duracion(duracion):
    try:
        valor = int(duracion)
        return valor > 0
    except ValueError:
        return False

def validar_calificacion(calificacion):
    try:
        valor = float(calificacion)
        return 0.0 <= valor <= 10.0
    except ValueError:
        return False

def mostrar_opciones():
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Agregar película")
    print("2. Buscar película")
    print("3. Eliminar película")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar películas")
    print("6. Salir")
    print("=====================================")

def obtener_opcion():
    opc = input("Seleccione una opción: ")
    if opc.isdigit():
        return int(opc)
    return 0


def agregar_pelicula(lista):
    titulo = input("Ingrese el título de la película: ")
    duracion = input("Ingrese la duración (minutos): ")
    calificacion = input("Ingrese la calificación (0.0 a 10.0): ")

    if not validar_titulo(titulo):
        print("Error: El título no puede estar vacío.")
    elif not validar_duracion(duracion):
        print("Error: La duración debe ser un entero mayor a cero.")
    elif not validar_calificacion(calificacion):
        print("Error: La calificación debe ser un decimal entre 0.0 y 10.0.")
    else:
        nueva_pelicula = {
            "titulo": titulo,
            "duracion": int(duracion),
            "calificacion": float(calificacion),
            "disponible": False 
        }
        lista.append(nueva_pelicula)
        print("Película registrada con éxito.")

def buscar_pelicula(lista, titulo_buscar):
    for i in range(len(lista)):
        if lista[i]["titulo"].lower() == titulo_buscar.lower():
            return i
    return -1

def actualizar_disponibilidad(lista):
    for pelicula in lista:
        if pelicula["calificacion"] >= 7.0:
            pelicula["disponible"] = True
        else:
            pelicula["disponible"] = False

peliculas = []  

while True:
    mostrar_opciones()
    opcion = obtener_opcion()

    if opcion == 1:
        agregar_pelicula(peliculas)

    elif opcion == 2:
        busqueda = input("Ingrese el título a buscar: ")
        posicion = buscar_pelicula(peliculas, busqueda)
        
        if posicion != -1:
            datos = peliculas[posicion]
            print(f"Película encontrada en posición {posicion}:")
            print(datos)
        else:
            print("Película no encontrada.")

    elif opcion == 3:
        busqueda = input("Ingrese el título de la película a eliminar: ")
        posicion = buscar_pelicula(peliculas, busqueda)
        
        if posicion != -1:
            peliculas.pop(posicion)
            print("Registro eliminado.")
        else:
            print(f"La película '{busqueda}' no se encuentra registrada.")

    elif opcion == 4:
        actualizar_disponibilidad(peliculas)
        print("Disponibilidad de todas las películas actualizada con éxito.")

    elif opcion == 5:
        actualizar_disponibilidad(peliculas)
        print("\n=== LISTA DE PELICULAS ===")
        for p in peliculas:
            estado = "DISPONIBLE" if p["disponible"] else "NO RECOMENDADA"
            print(f"Título: {p['titulo']}")
            print(f"Duración: {p['duracion']}")
            print(f"Calificación: {p['calificacion']}")
            print(f"Estado: {estado}")
            print("*" * 44)

    elif opcion == 6:
        print("Gracias por usar el sistema. Vuelva Pronto")
        break
    
    else:
        print("Opción no válida. Intente nuevamente.")