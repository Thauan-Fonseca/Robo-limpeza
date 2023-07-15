from stanfordkarel import *


def percorre_fronteira():
    move()
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()

def ir_diagonal():
    percorre_fronteira()
    turn_left()
    percorre_fronteira()
    

def virar_direita():
    turn_left()
    turn_left()
    turn_left()

def anda_seis():
    move()
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()
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
    run_karel_program()

