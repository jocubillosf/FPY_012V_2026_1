#EJERCICIO 1 

CantidadProfesores = 0 
ContadorTitular = 0
ContadorAsociado = 0 
Codigo = ''
Horas = 0

repetir = True

while repetir : 
    try:

        CantidadProfesores = int(input("ingrese cantidad de profesores :"))
        if CantidadProfesores > 0:
            repetir = False
        else:
            print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")
    except ValueError: 
         print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")

for contador in range(CantidadProfesores):

    print(" Registro Profesores ", contador + 1)
    CodigoValido = False

    while CodigoValido == False:
        Codigo = input("Ingrese el codigo docente:")
        if len(Codigo) >= 6 and '' not in Codigo:
            CodigoValido = True
        else:
            print("Codigo docente invalido")

repetirHoras = True

while repetirHoras:
    try:
        Horas = int(input("Ingrese horas catedras:"))
        
        if Horas> 0:
            repetirHoras = False
        else:
            print("¡Error académico! Ingresa un número entero positivo para las horas cátedra.")
    except :
        print("¡Error académico! Ingresa un número entero positivo para las horas cátedra.")

if Horas > 60:
    ContadorTitular = ContadorTitular + 1
else:
    ContadorAsociado = ContadorAsociado + 1
print("La universidad cuenta con", ContadorTitular,"profesores Titulares y", ContadorAsociado,"Profesores asociados, clases programadas")