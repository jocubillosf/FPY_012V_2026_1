horas = 0
cantprofes = int(input)
canthoras = 0
contador = 0
conttitular = 0
contasociado = 0

for x in range (1, cantprofes +1):
    print ("ingrese la cantidad de profesores")
    codigoProfesores = input()
    print ("ingrese cantidadd de horas")
    canthoras = int(input())
    if canthoras >=60:
        conttitular = conttitular + 1
    else:
        contasociado = contasociado + 1
        print("Usted es asociado")

print ("La cantidad de profesores titulares son ", conttitular)
print ("La cantidad de profesores asociados son ", contasociado)









