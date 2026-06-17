repetir = True
Asociados = 0
Titulares = 0
nuevosIngresos = 0

while True:
    try:
        valorProfesor = int(input("Ingrese el numero de profesores a ingresar: "))
        if valorProfesor > 0:
            break
        else:
            print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")
    except ValueError:
        print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")
        


#Registro Profesor 

mensaje = """
• Debe tener al menos 6 caracteres.
• No debe incluir espacios.
• Ejemplos válidos: DOC001PH, PROFMAX8, TEACHSCI3.
"""
print(mensaje)


#Codigo Docente
def validarLargo(clave):
    if len(clave) >=8:
        return True
    return False

def validarEspacio(clave):
    for caracter in clave:
        if caracter == '':
            return False
        return True
while repetir:
    clave= input("Ingrese su codigo: ")
    if validarEspacio(clave) and validarLargo(clave):
        print("Contraseña valida ")
        repetir = False 
    else:
        print("Contraseña invalida")

for nuevosIngresos in range (0,nuevosIngresos):
    print("Ingresa las horas de catedra del profesor")
    horasCatedra = int(input())
    if horasCatedra > 60:
        print("El profesor es Titular") 
        Titulares = Titulares+1
    else: 
        Asociados = Asociados +1

print(" La universidad cuenta con {Titulares} Profesores Titulares y {Asociados} Profesores Asociados! ¡Clases programadas")
    

        



