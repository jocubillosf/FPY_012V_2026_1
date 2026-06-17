repetir  = True
contadorTitulares = 0 
contadorAsociados = 0
while repetir:
    try:
        print("cuantos profesores desea registrar")
        cantidadProfesores = int (input())
        if cantidadProfesores > 0:
            repetir = False
        else:
            print ("Cantidad invalida, ingresa un entero positivo para continuar")
    except:
        print ("Cantidad invalida; ingresa un entero positivo para continuar")

for i in range (1,cantidadProfesores + 1):
    repetirCodigo = True
    while repetirCodigo:
        print("Ingrese codigo ", i)
        codigo = input()
        if len(codigo) >= 6:
            if ' ' in codigo:
                print("Debe ingresar un codigo sin espacios")
            else:
                repetirCodigo = False
        else:
            print("Debe ingresar codigo con al menos 6 caracteres")

repetirHoras = True
while repetirHoras:
    try:
        print("Ingrese horas catedra del profesor (entero positivo)")
        horasCatedra = int(input())
        if horasCatedra > 0:
            if horasCatedra <= 60:
                print("El profesor es asociado.")
                contadorAsociados += 1
            else:
                print("El profesor es titular.")
                contadorTitulares = contadorTitulares + 1
                repetirNivel = False
                
        else:
            print("¡Error academico!, ingresa un numero entero positivo para las horas catedra")
    except:
        print("¡Error academico!; ingresa un numero entero positivo para las horas catedra")

print("¡la universidad cuenta con", contadorTitulares, "Profesores titulares", contadorAsociados, "Profesores asociados")