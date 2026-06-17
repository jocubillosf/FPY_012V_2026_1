# Sistema de Gestión de Asientos para Sala de Conferencias

asientosDisponibles = 100
historialReservas = 0

print("¡Bienvenido al sistema de gestiones de asientos para la sala de Conferencias!")

while True:

    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Asientos disponibles")
    print("2. Reservar asientos")
    print("3. Liberar asientos")
    print("4. Historial de reservas")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    # OPCION 1
    if opcion == "1":
        print(f"Asientos disponibles: {asientosDisponibles}")

    # OPCION 2
    elif opcion == "2":

        try:
            cantidad = int(input("Ingrese la cantidad de asientos a reservar: "))

            if cantidad <= 0:
                print("Error: Debe ingresar un número mayor que cero.")

            elif cantidad > asientosDisponibles:
                print("No hay suficientes asientos disponibles para realizar la reserva.")

            else:
                asientosDisponibles -= cantidad
                historialReservas += cantidad
                print("Reserva realizada correctamente.")
                print(f"Asientos disponibles: {asientosDisponibles}")

        except ValueError:
            print("Error: Debe ingresar un número entero válido.")

    # OPCION 3
    elif opcion == "3":

        try:
            cantidad = int(input("Ingrese la cantidad de asientos a liberar: "))

            if cantidad <= 0:
                print("Error: Debe ingresar un número mayor que cero.")

            elif asientosDisponibles + cantidad > 100:
                print("Error: No se puede superar la capacidad máxima de 100 asientos.")

            else:
                asientosDisponibles += cantidad

                if historialReservas >= cantidad:
                    historialReservas -= cantidad
                else:
                    historialReservas = 0

                print("Asientos liberados correctamente.")
                print(f"Asientos disponibles: {asientosDisponibles}")

        except ValueError:
            print("Error: Debe ingresar un número entero válido.")

    # OPCION 4
    elif opcion == "4":
        print(f"Total de reservas realizadas durante la sesión: {historialReservas}")

    # OPCION 5
    elif opcion == "5":
        print("Gracias por utilizar nuestro software, hasta la próxima.")
        break

    # OPCION INVALIDA 
    else:
        print("Opción no válida. Intente nuevamente.")