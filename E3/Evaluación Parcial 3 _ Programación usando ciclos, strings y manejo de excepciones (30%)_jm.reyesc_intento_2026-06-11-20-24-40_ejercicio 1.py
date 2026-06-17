cant_profesores = 0
rep  = True
nom_doce = "" 
rep_nomb = True
rep_hrs = True
hrs = 0
cant_Titular = 0
cant_Asociado = 0
espacio = 0

while rep:

    try:
        print("Cuantos Profesores desea ingresar:")
        cant_profesores = int(input())
        print(cant_profesores)
        if cant_profesores > 0:
            rep = False
    except:
        print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")

for i in range(1,cant_profesores + 1):
   
   rep_nomb = True
   rep_hrs = True
   
   while rep_nomb:
        try:
             print("Ingrese el codigo del docente:")
             nom_doce = input()
             espacio = 0
             if len(nom_doce) >= 6:
                 for c in nom_doce:
                     if c == " ":
                         espacio += 1
                 if espacio == 0:
                     rep_nomb = False
                 else:
                     print("El Codigo del docente no debe contener espacios")
                         
        except:
            print("Codigo no valido, ingreselo nuevamente")

   while rep_hrs:
        
        try:
            print("Ingrese la horas de catedra del profesor:")
            hrs = int(input())
            if hrs > 0:
                if hrs <= 60:
                    print("El profesor es asociado")
                    cant_Asociado += 1
                else:
                    print("El profesor es Titular.")
                    cant_Titular += 1
                rep_hrs = False
        except:
            print("¡Error académico! Ingresa un número entero positivo para las horas cátedra.")

print("¡La universidad cuenta con",cant_Titular,"Profesores Titulares y cuenta con ",cant_Asociado,"Profesores Asociados! ¡Clases programadas!")