profesores = []
horasCatedra = []
codigo = []
def cant_prof():
    while True:
        try:
            numprof = int(input("Cuántos profesores desea agregar: "))
            if numprof < 0:
                print("No puede ingresar numeros negativos")
            else:
                return numprof
        except:
            print ("variable no válida")

def horas_catedra(titular, asociado):
    while True:
        try:
            horas = int(input("ingresar horas de catedra: "))
            if horas < 0:
                print("No puede ingresar numeros negativos")
            else:
                if horas_catedra() > 60:
                    titular += 1
                if horas_catedra() <= 60:
                    asociado += 1
                return titular, asociado
        except:
            print ("Error académico, ingresa un numero entero positivo")

def ingresar_profesor():
     codex = input("ingrese codigo docente: ")
     if len(codex) <= 5:
          print ("Demasiado corto, mínimo 6 caracteres")



titular = 0
asociado = 0


numprofesores = (cant_prof())

for cant_profesores in range(1,numprofesores+1):
    ingresar_profesor()
    titular, asociado = horas_catedra(titular, asociado)


print ("¡La universidad cuenta con ", titular, "profesores titulares, y ", asociado, "Profesores Asociados! ¡Clases programadas!")
