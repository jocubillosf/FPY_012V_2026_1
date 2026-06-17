opcion = 0
asientosDisponibles = 100
historialReservas = 0

while opcion != 5:

    print("=== MENÚ PRINCIPAL ===")
    print("1. Asientos disponibles")
    print("2. Reservar asientos")
    print("3. Liberar asientos")
    print("4. Historial de reservas")
    print("5. Salir")

    try:
        opcion = int(input("Seleccione opción: "))
    except ValueError:
        opcion = 0

    match opcion:

        case 1:
            print("Asientos disponibles:", asientosDisponibles)

        case 2:

            repetir = True

            while repetir:
                try:
                    cantidad = int(input("Cantidad de asientos a reservar: "))

                    if cantidad <= 0:
                        print("Debe ingresar un número mayor a 0")

                    elif cantidad > asientosDisponibles:
                        print("No hay suficientes asientos disponibles")

                    else:
                        asientosDisponibles = asientosDisponibles - cantidad
                        historialReservas = historialReservas + cantidad
                        print("Reserva realizada correctamente")
                        repetir = False

                except ValueError:
                    print("Debe ingresar un número entero")

        case 3:

            repetir = True 
            
            while repetir:
                try:
                    cantidad = int(input("Cantidad de asientos a liberar: "))

                    if cantidad <= 0:
                        print("Debe ingresar un número mayor a 0")

                    elif asientosDisponibles + cantidad > 100:
                        print("No puede superar la capacidad máxima")

                    else:
                        asientosDisponibles = asientosDisponibles + cantidad
                        historialReservas = historialReservas - cantidad

                        if historialReservas < 0:
                            historialReservas = 0

                        print("Asientos liberados correctamente")
                        repetir = False

                except ValueError:
                    print("Debe ingresar un número entero")
        case 4:
            print("Historial de reservas:", historialReservas)

        case 5:
            print("Gracias por utilizar nuestro software, hasta la próxima.")

        case _:
            print("Debe ingresar una opción válida")