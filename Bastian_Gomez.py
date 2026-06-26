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
    opcion=int(input("Ingrese una opcion"))