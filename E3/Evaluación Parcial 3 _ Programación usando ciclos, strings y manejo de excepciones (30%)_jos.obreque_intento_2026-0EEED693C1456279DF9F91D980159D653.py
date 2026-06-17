profesores=0
i=0
CodigoDocente=0
ContadorAsociado=0
ContadorTitular=0
while True:
    try:
        profesores=int(input("Ingrese la cantidad de profesores\n"))
        if profesores<=0:
            print("¡Cantidad inválida! Ingresa un entero positivo para continuar")
        else:
            print("cantidad registrada con exito")
            break
    except:
        print("¡Cantidad inválida! Ingresa un entero positivo para continuar")

for i in range(1,profesores+1):
    while True:
        try:
            CodigoDocente=input(f"ingrese el codigo del docente {i}\n",)
            if len(CodigoDocente)<6:
                print("Ingrese al menos 6 caracteres")
            elif " " in CodigoDocente:
                print("No debe contener espacios")
            else:
                print("codigo docente guardado con exito")
                break
        except:
            print("Ingrese al menos 6 caracteres\nno debe de contener espacio")

for a in range(1,profesores+1):
    while True:
        try:
            horasCatedra=int(input("Ingrese las horas del docente: \n"))
            if horasCatedra<=0:
                print("¡Error académico! Ingresa un número entero positivo para las horas cátedra")
            else:
                print("hora/s registrada/s con exito")
                break
        except:
            print("¡Error académico! Ingresa un número entero positivo para las horas cátedra")

    if horasCatedra<=60:
        print(f"El profesor {a} es Asociado")
        ContadorAsociado+=1
    else:
        print(f"el profesor {a} es titular")
        ContadorTitular+=1

print(f"¡La universidad cuenta con {ContadorTitular} Profesores Titulares y {ContadorAsociado} Profesores Asociados! ¡Clasesprogramadas!")