opcion=0
ASIENTOS=100
asientosTotales=ASIENTOS
ElegirAsiento=0
ContadorReserva=0
print("¡Bienvenido al sistema de gestión de asientos de la Sala de Conferencias!")
print("=== MENÚ PRINCIPAL ===")
print("1.	Asientos disponibles")
print("2.	Reservar asientos")
print("3.	Liberar asientos")
print("4.	Historial de reservas")
print("5.	Salir")
while opcion !=5:
    opcion=int(input("Ingrese una opcion:\n"))
    match opcion:
        case 1:
            print(f"Hay un total de {asientosTotales} Asientos disponibles")
        case 2:
            while True:
                try:
                    ElegirAsiento=int(input("ingrese la cantidad de asientos que desea reservar\n"))
                    if ElegirAsiento<=0 or ElegirAsiento>asientosTotales:
                        print("Ingrese un valor válido")
                    else:
                        print("Asiento registrado con éxito")
                        asientosTotales=asientosTotales-ElegirAsiento
                        break
                except:
                    print("ingrese un valor válido")
        case 3:
            while True:
                if ElegirAsiento==0:
                    print("no a reservado asientos para cancelar")
                    print("redirigiendo al menú...")
                    break
                else:
                    print("espere un momento...")
                try:
                    print(f"usted posee {ElegirAsiento} Asientos para liberar")
                    LiberarAsiento=int(input("Ingrese la cantidad de asientos a liberar:\n"))
                    if LiberarAsiento<=0 or LiberarAsiento>ASIENTOS:
                        print("ingrese un valor válido")
                    else:
                        print("asiento liberado con éxito")
                        asientosTotales=asientosTotales+LiberarAsiento
                        
                        ElegirAsiento=ElegirAsiento-LiberarAsiento
                        break
                except:
                    print("ingrese un valor válido")
        case 4:
            print(f"usted a reservado {ElegirAsiento} Asientos actualmente")

print("Gracias por utilizar nuestro software, hasta la próxima.")