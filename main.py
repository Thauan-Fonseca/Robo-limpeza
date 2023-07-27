from stanfordkarel import *


def percorre_fronteira():
    for cont in range(7):
        move()
        put_beeper()

def ir_diagonal():
    percorre_fronteira()
    turn_left()
    percorre_fronteira()
    

def virar_direita():
    for cont in range(3):
        turn_left()


def anda_seis():
    for cont in range(6):
        move()
        put_beeper()

def zig_zag_vertical():
    turn_left()
    move()
    put_beeper()
    turn_left()
    anda_seis()
    virar_direita()
    move()
    put_beeper()
    virar_direita()
    anda_seis()


def main():
    """Karel code goes here!"""

    #Varredura Uniforme
    ir_diagonal()
    zig_zag_vertical()
    zig_zag_vertical()
    zig_zag_vertical()
    turn_left()
    move()
    put_beeper()
    turn_left()
    percorre_fronteira()
    turn_left()
    

if __name__ == "__main__":
    run_karel_program('.\maze_8x8_type_I.w')

