titular = 0
asociado = 0

while True:
  try:
    docentes = int(input("Ingrese la cantidad de profesores a registrar: "))
    if docentes <= 0:
      print("¡Cantidad inválida! Ingresa un entero positivo para continuar")
    else:
      break
  except ValueError:
    print("¡Cantidad inválida! Ingresa un entero positivo para continuar")


print("---Código del docente---")

for i in range(docentes):
       while True:
        codigo_docente = input(f"Ingrese nombre del profesional {i+1}:")
        if len(codigo_docente) < 6 or " " in codigo_docente:
            print("Error: El código debe tener al menos 6 caracteres y no contener espacios en blanco.")
        else:
            break

print("---Horas de cátedra---")
for i in range(docentes):
    while True:
        try:
            horas = int(input(f"Ingrese la cantidad de horas de cátedra del docente {i+1}: "))
            if horas <= 0:
                print("¡Error académico! Ingresa un número entero positivo para las horas cátedra.")
            else:
                break
        except ValueError:
            print("¡Error académico! Ingresa un número entero positivo para las horas cátedra.")

    print("---Clasificación del Profesor---")
    if horas <= 60:
        print(f"El profesor {i} es Asociado")
        asociado += 1
    else:
        print(f"El profesor {i+1} es Titular")
        titular += 1


print(f"¡La universidad cuenta con {titular} Profesores Titulares y {asociado} Profesores Asociados! ¡Clases programadas!")









































  

