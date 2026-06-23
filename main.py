op = 0

while op != 4:
    print("======MENU APUESTAS======")
    print("1- Ver partidos disponibles")
    print("2- Apostar en un partido")
    print("3- Ver resumen de apuestas")
    print("4- Salir")

    match op:
        case 1:
            verpartidos()
        case 2:
            apostar()
        case 3:
            veresumen()
        case 4:
            print("Saliendo del menu de apuestas")
        case _:
            print("Ingresa una opcion valida")
    
