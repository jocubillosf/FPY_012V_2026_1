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

def apostar(partidos):
    


def veresumen():

