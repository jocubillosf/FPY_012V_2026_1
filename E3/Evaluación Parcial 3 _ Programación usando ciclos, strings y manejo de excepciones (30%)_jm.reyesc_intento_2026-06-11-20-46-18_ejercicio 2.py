asientos = 100
asientos_reservados = 0
cant = 0
op = 0

print("¡Bienvenido al sistema de gestión de asientos de la Sala de Conferencias!")

while op != 5:

    print("=== MENÚ PRINCIPAL ===")
    print("1.	Asientos disponibles")
    print("2.	Reservar asientos")
    print("3.	Liberar asientos")
    print("4.	Historial de reservas")
    print("5.	Salir")
    op = int(input())

    match op:

        case 1:
            print("la cantidad de asientos disponibles es:",asientos)
        case 2:
            if asientos != 0:
                val = True
                while val:   
                    try:
                        print("Cuantos asientos desea reservar:")
                        cant = int(input())
                        if cant < asientos and cant > 0:
                            print("Asientos reservados.")
                            asientos -= cant
                            asientos_reservados += cant
                            val = False
                        else:
                            print("Ingrese otra cantidad")
                    except:
                        print("Ingrese otra cantidad valida.")
        case 3:
            try:
                print("Cuantos asientos desea liberar:")
                cant = int(input())
                
                if cant < asientos and cant > 0:
                    print("Asientos liberados.")
                    asientos += cant
                    asientos_reservados -= cant
                else:
                    print("Ingrese otra cantidad.")
            except:
                print("Ingrese otra cantidad valida.")

        case 4:
            print("Historial de Reservas:")
            print("En este momento hay:",asientos_reservados,"Asientos reservados")

        case 5:
            print("Gracias por utilizar nuestro software, hasta la próxima.")

        case _:
            print("Ingrese una opcion valida")
            
        
                        
                    

