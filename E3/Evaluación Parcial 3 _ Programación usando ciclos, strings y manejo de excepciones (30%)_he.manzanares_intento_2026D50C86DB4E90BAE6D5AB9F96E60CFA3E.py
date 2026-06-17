#EJERCICIO1HECTOR
repetir= True
contadortitular=0
contadorasociado=0
cantidadprofesores=0
codigoprofesor=0

while repetir:
    try:
        print("Ingrese los profesores a registrar")
        cantidadprofesores= int(input())
        if cantidadprofesores >= 0:
            repetir=False
        else:
            print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")
    except:
        print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")

for i in range(1,cantidadprofesores + 1):
    repetircodigo = True
    while repetircodigo:
        print("Ingrese su código de Profesor")
        codigoprofesor= input()
        if len(codigoprofesor) >=6:
            if ' ' in codigoprofesor:
                print("Debe ingresar un nombre sin espacios")
            else:
                repetircodigo= False
        else:
            print("Debe ingresar nombre con al menos 6 caracteres.")
    
    repetirhoras = True
    while repetirhoras:
        try:        
            print("Ingrese sus horas con un número entero positivo")
            cantidadhoras= int(input())
            if cantidadhoras > 0:
                if cantidadhoras <= 60:
                    print("Usted es Profesor Asociado")
                    contadorasociado += 1
                else:
                    print("Usted es Profesor Titular")
                    contadortitular = contadortitular + 1
                repetirhoras= False
            else:
                print("¡Error académico! Ingresa un número entero positivo para las horas cátedra.")
        except ValueError:
            print("¡Error académico! Ingresa un número entero positivo para las horas cátedra.")
print("¡La universidad cuenta con ", contadortitular ,"Profesores Titulares y", contadorasociado, "Profesores Asociados! ¡Clases programadas!")





            