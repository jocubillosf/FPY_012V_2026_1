#EJERCICIO1_ALEXIS_DIAZ

total_titulares = 0
total_asociados = 0


while True:
    try:
        cantidad_profesores = int(input("Ingrese la cantidad de profesores que desea registrar: "))
        if cantidad_profesores > 0:
            break
        else:
            print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")
    except ValueError:
            print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")


for i in range(5):
    print(f"\n--- Registrando profesor {i + 1} de {cantidad_profesores} ---")

while True:
    codigo_docente = input("Ingrese el Código Docente: ")
    if len(codigo_docente) >= 6 and " " not in codigo_docente:
        break
    else:
        print("Código inválido. Debe tener al menos 6 caracteres y no incluir espacios.")
        
while True:
    try:
        horas_catedra = int(input("Ingrese las horas cátedra del profesor: "))
        if horas_catedra > 0:
            break
        else:
            print("¡Error académico! Ingresa un número entero positivo para las horas cátedra.")
    except ValueError:
            print("¡Error académico! Ingresa un número entero positivo para las horas cátedra.")


if horas_catedra > 60:
    total_titulares += 1
else:
    total_asociados += 1
print(f"¡La universidad cuenta con {total_titulares} Profesores Titulares y {total_asociados} Profesores Asociados! ¡Clases programadas!")