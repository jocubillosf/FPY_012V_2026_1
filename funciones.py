import equipos 

partidos = {
    "Grupo K": [(equipos.team_portugal,equipos.team_uzbekistan)],
    "Grupo D": [(equipos.team_inglaterra,equipos.team_ghana)],
    "Grupo F": [(equipos.team_panama,equipos.team_croacia)],
    "Grupo H": [(equipos.team_colombia,equipos.team_congo)]
}

def verpartidos(partidos):

    for grupo, parti in partidos.items():
        print(f"\n {grupo}")
        print("="* 40)
        for team1, team2 in parti:
            print(team1["nombre"], "vs",team2["nombre"])
            print(team1)
            print(team2)

def apuestas(op,apu):


def apostar(partidos):
    op = 0
    apu = 0
    apuestas = []
    while op != 5:
        print("En que grupo deseas apostar??:")
        print("1-Grupo K")
        print("2-Grupo D")
        print("3-Grupo F")
        print("4-Grupo H")
        print("5-Salir")
        op = int(input())

        match op:
            case 1:
                print("Grupo K")
                print("1-Portugal")
                print("2-uzbekistan")
                print("Por cual desea apostar??")
                apu = int(input())
                apuestas(op,apu)
            case 2:

            case 3:
            
            case 4:

            case 5:

            case _:
                print("Ingrese una opcion valida.")




def veresumen():

