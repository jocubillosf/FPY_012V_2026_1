repetir = True
contadorAsociado = 0
cantidadProfesores = 0
contadorTitular = 0

while repetir:
    try:
        print("Cuantos profesores desea ingresar: ")
        cantidadProfesores = int(input())
        if cantidadProfesores > 0:
            repetir = False
        else:
            print("¡Cantidad inválida! Ingresa un entero positivo para continuar")
    except:
        print("¡Cantidad inválida! Ingresa un entero positivo para continuar")

for i in range(1,cantidadProfesores + 1):
    repetirCodigo = True
    while repetirCodigo:
        print("Ingrese Codigo Docente ", i)
        codigoDocente = input()
        if len(codigoDocente) >= 6:
            if ' ' in codigoDocente:
                print("Debe ingresar un codigo sin espacios")
            else:
                repetirCodigo = False
        else:
            print("Debe ingresar codigo con al menos 6 caracteres")
    repetirHoras = True
    while repetirHoras:
        try:
            print("Ingrese las horas cátedra del profesor (entero positivo)")
            horasCatedra = int(input())
            if horasCatedra > 0:
                if horasCatedra > 60:
                    print("El profesor es titular.")
                    contadorTitular += 1
                else:
                    print("El profesor es asociado.")
                    contadorAsociado = contadorAsociado + 1
                repetirHoras = False 
            else:
                print("¡Error academico! Ingresa un número entero positivo para las horas catedra")
        except ValueError:
            print("¡Error academico! Ingresa un número entero positivo para las horas catedra")

print("¡La universidad cuenta con  ", contadorTitular ," Profesores Titulares y ", contadorAsociado , " Profesores Asociados ! ¡Clases programadas!")
