cantidadProfesores=0
contadorTitulares=0
contadorAsosiados=0

# VALIDAR CANTIDAD DE PROFESORES 
while True:
    try:
        cantidadProfesores = int(input("¿Cuantos profesores desea registrar?: "))

        if cantidadProfesores > 0:
            break
        else:
            print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")

    except ValueError:
        print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")

# CONTADORES
titulares = 0
asociados = 0

# REGISTRO PROFESORES
for i in range(1, cantidadProfesores + 1):

    
    print("Registro del Profesor", i)
    

    # VALIDAR CODIGO DOCENTE 
    while repetir:
        codigo = input("Ingrese el código docente: ")

        if ValidarCodigo (codigo:)
            break
        else:
            print("Código inválido. Debe tener al menos 6 caracteres y no contener espacios.")

    # VALIDAR CANTIDAD DE CATEDRAS 
    while True:
        try:
            horas = int(input("Ingrese las horas cátedra: "))

            if horas > 0:
                break
            else:
                print("¡numero invalido! Ingresa un número entero positivo para las horas cátedra.")

        except ValueError:
            print("¡numero invalido! Ingresa un número entero positivo para las horas cátedra.")

    # CLASIFICACION
    if horas > 60:
        categoria = "Titular"
        titulares += 1
    else:
        categoria = "Asociado"
        asociados += 1

    print("Profesor clasificado como:", categoria)

# RESUMEN FINAL 
print("RESUMEN DE REGISTRO")
print("Total de profesores registrados:", cantidadProfesores)
print("Profesores Titulares:", titulares)
print("Profesores Asociados:", asociados)
print(f"¡La universidad cuenta con {titulares} Profesores Titulares y {asociados} Profesores Asociados! ¡Clases preparadas!")