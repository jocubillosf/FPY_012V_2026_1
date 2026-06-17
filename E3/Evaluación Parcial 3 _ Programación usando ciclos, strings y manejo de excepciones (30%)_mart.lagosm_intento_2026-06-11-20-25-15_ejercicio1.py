cantidadProfesores = 0
contadorTitulares = 0
contadorAsociados = 0

def validarCodigo(codigo):
    if len(codigo) >= 6 and ' ' not in codigo:
        return True
    return False

# CANTIDAD DE PROFESORES
repetir = True

while repetir:
    try:
        cantidadProfesores = int(input("Ingrese cantidad de profesores: "))

        if cantidadProfesores > 0:
            repetir = False
        else:
            print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")

    except ValueError:
        print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")

# REGISTRO
for i in range(cantidadProfesores):

    print(" Profesor", i + 1, )

    repetir = True

    while repetir:
        codigo = input("Ingrese código docente: ")

        if validarCodigo(codigo):
            repetir = False
        else:
            print("Código inválido")

    repetir = True

    while repetir:
        try:
            horas = int(input("Ingrese horas cátedra: "))

            if horas > 0:
                repetir = False
            else:
                print("¡Error académico! Ingresa un número entero positivo para las horas cátedra.")

        except ValueError:
            print("¡Error académico! Ingresa un número entero positivo para las horas cátedra.")

    if horas > 60:
        contadorTitulares += 1
    else:
        contadorAsociados += 1

# SALIDA FINAL
print("La universidad cuenta con",
      contadorTitulares,
      "Profesores Titulares y",
      contadorAsociados,
      "Profesores Asociados, clases programadas")
