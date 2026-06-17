

horasCatedra = 0
nuevosIngresos = 0
titulares = 0
asociados = 0
contTitulares = 0
contAsociados = 0
codigoDoc = ''




print("REGISTRO DE NUEVOS INGRESOS DE PROFESORES")
nuevosIngresos = int(input("Ingrese la cantidad de docentes a registrar: "))

for nuevosIngresos in range(0, nuevosIngresos):
    print("Ingrese las horas catedra del docente: ")
    horasCatedra = int(input())
    if horasCatedra <= 60:
        contAsociados = contAsociados + 1
    elif horasCatedra > 60:
        contTitulares = contTitulares + 1
        

    print("Ingrese codigo docente")
    codigoDoc = str(input())
    if len(codigoDoc) < 6 or " " in codigoDoc:
        print("El codigo debe de tener al menos 6 caracteres y no debe tener espacios")
    else:
        print("El codigo ingresado es correcto")
        
    
print("¡La universidad cuenta con", contTitulares ,"Profesores Titulares y", contAsociados, "Profesores Asociados! ¡Clases programadas!")
    
