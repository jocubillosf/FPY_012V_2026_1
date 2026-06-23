import equipos 

partidos = [
    (equipos.team_portugal,equipos.team_uzbekistan),
    (equipos.team_inglaterra,equipos.team_ghana),
    (equipos.team_panama,equipos.team_croacia),
    (equipos.team_colombia,equipos.team_congo)
    ]

def verpartidos(partidos):

    for team1, team2 in partidos:
        print(team1["nombre"], "vs",team2["nombre"])
        print(team1)
        print(team2)

def apostar():


def veresumen():

    