print("Ingrese cantidad de profesores")
codigoProfesor = 0
cantProfesores = int(input)
contadorTitular = 0
contadorAsociado = 0

for x in range (1, cantProfesores + 1):
    print("Ingrese codigo de profesor")
    codigoProfesor = input()
    print("Ingrese cantidad de horas")
    cantHoras = int(input())
    if cantHoras > 60:
        contadorTitular = contadorTitular + 1
    else:
        contadorAsociado = contadorAsociado + 1

print("Cantidad de profesores tirulados son: ", contadorTitular)
print("Cantidad de profesores asociados son: ", contadorAsociado)



