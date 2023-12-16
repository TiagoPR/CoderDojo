import random

NORTH = "N"
SOUTH = "S"
EAST =  "E"
WEST = "O"

def get_direction():
    dir = input("Que direção pretendes seguir? [N/S/E/O]\n").upper()
    if dir == "N" or dir == "NORTE" or dir == "NORTH":
        return NORTH
    elif dir == "S" or dir == "SUL" or dir == "SOUTH":
        return SOUTH
    elif dir == "E" or dir == "ESTE" or dir == "EAST":
        return EAST
    elif dir == "O" or dir == "OESTE" or dir == "WEST":
        return WEST
    else:
        print("O input não está correto, tenta de novo")
        get_direction()


def boss_fight():
    score = 0
    print("")
    while score <= 3:
        print("randomint(1,10)")