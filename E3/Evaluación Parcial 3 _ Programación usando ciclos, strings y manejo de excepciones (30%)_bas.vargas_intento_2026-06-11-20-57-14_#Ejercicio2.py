#Ejercicio2
import time
print("¡Bienvenido al sistema de gestión de asientos de la Sala de Conferencias!")

Asientos_disponibles = 100
max_asientos = 100
contador_historial = 0


def Reserva_asientos():
    global Asientos_disponibles
    global contador_historial
    reserva_invalida = True
    Asientos_reservar = 0

    while reserva_invalida:
        try:
            print()
            print("***RESERVAR ASIENTOS***")
            print("Ingrese cuantos asientos desea reservar: ")
            Asientos_reservar = int(input(":"))
            if Asientos_reservar < 0:
                print("¡ERROR! Ingrese un número entero positivo")
            elif Asientos_reservar > Asientos_disponibles:
                print("¡ERROR! la cantidad ingresada supera los asientos disponibles")
            
            else:
                Asientos_disponibles -= Asientos_reservar
                contador_historial += Asientos_reservar
                print("Reserva valida")
                print(f"Ha reservado {Asientos_reservar} asientos/s")
                reserva_invalida = False




        except ValueError:
            print("¡ERROR! Ingrese un número entero positivo")

def Liberar_asientos():
    global Asientos_disponibles
    global contador_historial
    Cantidad_liberar = 0
    Liberar = True
    suma_temporal = 0
    while Liberar:
        try:
            print()
            print("***LIBERAR ASIENTOS***")
            print("Ingrese cuantos asientos desea liberar: ")
            Cantidad_liberar = int(input(":"))
            suma_temporal = Asientos_disponibles + Cantidad_liberar
            if Cantidad_liberar < 0:
                print("¡ERROR! Ingrese un número entero positivo")
            elif suma_temporal > max_asientos:
                print("¡ERROR! la cantidad ingresada supera la cantidad de asientos maximos disponibles")
            elif Cantidad_liberar > Asientos_disponibles:
                print("¡ERROR! Los asientos disponibles superan los aientos disponibles")
            else:
                Asientos_disponibles += Cantidad_liberar
                contador_historial -= Cantidad_liberar
                print("Liberación realziada con éxito")
                print(f"Asientos liberados con éxito: {Cantidad_liberar}")
                Liberar  = False
        except ValueError:
            print("¡ERROR! Ingrese un número entero positivo")

def Historial_reserv():
    print()
    print("***HISTORIAL RESERVAS***")
    print(f"Las reservas hechas en esta sesión son: {contador_historial}")
    print()



def Menu_principal():
    global Asientos_disponibles
    opciones = True
    opc = 0


    while opciones:
        try:
            print()
            print("=== MENU PRINCIPAL ===")
            print("1)Asientos disponibles\n2)Reservar asientos\n3)Liberar asientos\n4)Historial de reservas\n5)Salir")
            opc = int(input(":"))
            if opc < 0:
                print("¡ERROR! Numero ingresado invalido, ingrese un numero entero positivo")
            else:
                match opc:
                    case 1:
                        print()
                        print("***ASIENTOS DISPONIBLES***")
                        print(f"Asientos disponibles: {Asientos_disponibles}")
                        print()
                    case 2:
                        Reserva_asientos()
                    case 3:
                        Liberar_asientos()
                    case 4:
                        Historial_reserv()
                    case 5:
                        print()
                        print("Gracias por utilizar nuestro software, hasta la próxima.")
                        time.sleep(0.5)
                        print(" Cerrando.")
                        time.sleep(1)
                        print(" Cerrando..")
                        time.sleep(1)
                        print(" Cerrando...")
                        time.sleep(1)
                        print("¡Cerrado de programa con éxito!")
                        opciones = False
                    case _:
                        print("Opción no encontrada")
                        
                    
        except ValueError:
            print("¡ERROR! Numero ingresado invalido, ingrese un numero entero positivo")

Menu_principal()