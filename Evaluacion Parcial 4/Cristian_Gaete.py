lista_peliculas = []

def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar película")
    print("2. Buscar película")
    print("3. Eliminar película")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar películas")
    print("6. Salir")
    print("=====================================")

def leer_opcion():
    try:
        opcion = int(input("Ingrese una opción: "))
        if opcion < 1 or opcion > 6:
            print("Opción inválida")
        else:
            return opcion
    except ValueError:
        print("Opción inválida")

# ====================================================

def validar_titulo(titulo):
    titulo_limpio = titulo.strip() # elimina espacios en los límites
    while "  " in titulo_limpio:
        titulo = titulo_limpio.replace("  ", " ") # elimina espacios interiores
    if titulo_limpio == "":
        return False
    else:
        return True

def validar_duracion(duracion):
    if duracion > 0:
        return True
    else:
        return False

def validar_calificacion(calificacion):
    if calificacion >= 0.0 and calificacion <= 10.0:
        return True
    else:
        return False

# ====================================================

def agregar_pelicula(lista):
    titulo = input("Ingrese titulo de la película: ")
    while True:
        try:
            duracion = int(input("Ingrese duración de la película: "))
            break
        except ValueError:
            print("Error de formato: La duración debe ser un número entero.")
    while True:
        try:
            calificacion = float(input("Ingrese la calificacion: "))
            break
        except ValueError:
            print("Error de formato: La calificacion debe ser un número.")
    if validar_titulo(titulo) == False:
        print("Error: Titulo no válido.")
    elif validar_duracion(duracion) == False:
        print("Error: Duración no válida.")
    elif validar_calificacion(calificacion) == False:
        print("Error: calificacion no válida.")    
    else:
        peliculas = {
            "titulo": titulo,
            "duracion": duracion,
            "calificacion": calificacion,
            "disponible": True
        }
        lista.append(peliculas)
        print("Pelicula registrada correctamente.")

# ====================================================

def buscar_pelicula(lista, titulo):
    for i in range(len(lista)):
        if lista[i]["titulo"] == titulo:
            return i
    return -1

# ====================================================

def eliminar_pelicula(lista):
    titulo_a_buscar = input("Ingrese el titulo de la película a eliminar: ")
    posicion = buscar_pelicula(lista, titulo_a_buscar)
    
    if posicion != -1:
        lista.pop(posicion)
        print("Película eliminada.")
    else:
        print(f"La película '{titulo_a_buscar}' no se encuentra registrada.")

# ====================================================

def actualizar_disponibilidad(lista):
    for pelicula in lista:
        if pelicula["calificacion"] >= 7.0:
            pelicula["disponible"] = True
        else:
            pelicula["disponible"] = False

# ====================================================

def mostrar_pelicula(lista):
    actualizar_disponibilidad(lista)
    print("=== LISTA DE PELICULAS ===")
    for pelicula in lista:
        if pelicula["disponible"] == True:
            texto_estado = "DISPONIBLE"
        else:
            texto_estado = "NO RECOMENDADA"   
        print(f"titulo: {pelicula['titulo']}")
        print(f"duracion: {pelicula['duracion']}")
        print(f"calificacion: {pelicula['calificacion']}")
        print(f"disponible: {texto_estado}")
        print("********************************************")

# ====================================================

while True:
    mostrar_menu()
    opcion_elegida = leer_opcion()
    
    if opcion_elegida == 1:
        agregar_pelicula(lista_peliculas)
        
    elif opcion_elegida == 2:
        nombre_buscado = input("Ingrese el nombre de la película a buscar: ")
        posicion = buscar_pelicula(lista_peliculas, nombre_buscado)
        if posicion != -1:
            pelicula_encontrada = lista_peliculas[posicion]
            print(f"Película encontrada en la posición {posicion}:")
            print(f"Titulo: {pelicula_encontrada['titulo']}, Duracion: {pelicula_encontrada['duracion']}, calificacion: {pelicula_encontrada['calificacion']}")
        else:
            print("Película no encontrado.")
            
    elif opcion_elegida == 3:
        eliminar_pelicula(lista_peliculas)
        
    elif opcion_elegida == 4:
        actualizar_disponibilidad(lista_peliculas)
        print("Disponibilidad actualizada.")
        
    elif opcion_elegida == 5:
        mostrar_pelicula(lista_peliculas)
        
    elif opcion_elegida == 6:
        print("Gracias por usar el sistema. Vuelva Pronto")
        break
        
    else:
        print("Opción no válida. Intente nuevamente.")