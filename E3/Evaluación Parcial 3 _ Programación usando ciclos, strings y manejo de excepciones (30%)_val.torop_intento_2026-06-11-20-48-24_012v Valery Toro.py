def validar_entero_positivo(mensaje_error):
    """Valida que el usuario ingrese un número entero positivo."""
    while True:
        try:
            valor = int(input())
            if valor > 0:
                return valor
            else:
                print(mensaje_error)
        except ValueError:
            print(mensaje_error)

def validar_codigo_docente():
    """Valida que el código del docente tenga al menos 6 caracteres y no incluya espacios."""
    while True:
        codigo = input("Ingresa el código del docente (mínimo 6 caracteres, sin espacios): ")
        if len(codigo) >= 6 and " " not in codigo:
            return codigo
        else:
            print("¡Código inválido! Asegúrate de que tenga al menos 6 caracteres y no incluya espacios.")

def clasificar_profesor(horas):
    """Clasifica al profesor como Titular o Asociado según las horas cátedra."""
    if horas > 60:
        return "Titular"
    else:
        return "Asociado"

def main():
    print("¿Cuántos profesores deseas registrar?")
    cantidad_profesores = validar_entero_positivo("¡Cantidad inválida! Ingresa un entero positivo para continuar.")

    titulares = 0
    asociados = 0

    for i in range(cantidad_profesores):
        print(f"\nRegistro del profesor {i + 1}:")
        codigo = validar_codigo_docente()
        print("Ingresa las horas cátedra del profesor:")
        horas_catedra = validar_entero_positivo("¡Error académico! Ingresa un número entero positivo para las horas cátedra.")
        
        clasificacion = clasificar_profesor(horas_catedra)
        if clasificacion == "Titular":
            titulares += 1
        else:
            asociados += 1

    print(f"\n¡La universidad cuenta con {titulares} Profesores Titulares y {asociados} Profesores Asociados! ¡Clases programadas!")

if __name__ == "__main__":
    main()