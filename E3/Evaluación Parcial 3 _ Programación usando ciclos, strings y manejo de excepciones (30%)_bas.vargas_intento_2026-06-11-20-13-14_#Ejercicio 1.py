#Ejercicio 1
num_docente = 0
bucle1 = True
num_docente = 0
contador_Titular = 0
contador_Asociado = 0

def Horas_catedra():
    global contador_Titular
    global contador_Asociado
    Horas_invalidas = True
    while Horas_invalidas:
        try:
            print("Ingrese las horas de catedra: ")
            Horas_catedra = int(input(":"))
            if Horas_catedra < 0:
                print("¡Error académico! Ingresa un número entero positivo para las horas cátedra.")
            else:
                if Horas_catedra > 60:
                    contador_Titular += 1
                    Horas_invalidas = False
                    
                elif Horas_catedra <= 60:
                    contador_Asociado += 1
                    Horas_invalidas = False


        except ValueError:
            print("¡Error académico! Ingresa un número entero positivo para las horas cátedra.")


def validar_largo(cod_docente):
    Largo = len(cod_docente)
    MIN_CARACTERES = 6
    if Largo < MIN_CARACTERES:
        print("Codigo demasiado corto")
        return True
    else:
        return False

def Validar_espacios(cod_docente):
    MAX_ESPACIOS = 0
    contador_espacios = 0
    for letra in cod_docente:
        if letra.isspace():
            contador_espacios += 1
    if contador_espacios > MAX_ESPACIOS:
        print("El código no puede contener espacios")
        return True
    else:
        return False


def codigo_docente(num_docente):
    vueltas = 0
    while vueltas < num_docente:
        codigo_invalido = True
        while codigo_invalido:
            print()
            print("Ingrese el codigo del docente: ")
            cod_docente = input(":")
            if validar_largo(cod_docente) or Validar_espacios(cod_docente):
                print("Código invalido")
            else:
                print("Código valido")
                vueltas += 1
                Horas_catedra()
                codigo_invalido = False
    print(f"¡La universidad cuenta con {contador_Titular} Profesores Titulares y {contador_Asociado} Profesores Asociados! ¡Clases pro-gramadas!")



while bucle1:
    try:
        print("Ingrese la cantidad de profesores que desea registrar: ")
        num_docente = int(input(":"))
        if num_docente < 0:
            print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")
        else:
            print()
            codigo_docente(num_docente)
            bucle1 = False
            


    except ValueError:
        print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")