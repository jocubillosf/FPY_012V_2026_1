#Administracion de registro
repetir = True
total_titulares = 0
total_asociados = 0

print("=== Bienvenido al registro de nuevos ingresos ===")
while repetir:
    try:
        cantidad_profesores = int(input("Ingrese Cantidad de profesores a registrar: "))
        if cantidad_profesores > 0:
             repetir = False
        else:
            print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")
    
    except: 
     print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")
    
    
    
for i in range(1, cantidad_profesores + 1):
    repetirCodigo = True
    while repetirCodigo:
        print("Ingresa Codigo del docente",i)
        codigo =input()
        if len(codigo) >= 6:
            if ' ' in codigo:
                print("Debe ingresar un nombre sin espacios ")
            else:
                repetirCodigo = False
        else:
            print("Debe ingresar nombre con al menos 6 caracteres")

    repetirHoras = True
    while repetirHoras:
        try:
            print("Ingrese horas de la Catedra (Entero Positivo)")
            horas = int(input())
            if horas > 0:
                if horas > 60:
                 total_titulares = total_titulares + 1
                else:
                    total_asociados = total_asociados +1
                repetirHoras = False
            else:
                print("¡Error académico! Ingresa un número entero positivo para las horas cátedra.")
        except:
            print("¡Error académico! Ingresa un número entero positivo para las horas cátedra.")

print("¡La universidad cuenta con", total_titulares, "Profesor/es Titulares y", total_asociados, "Profesores Asociados! ¡Clases programadas!")