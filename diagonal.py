from stanfordkarel import *

# Realizar uma varredura diagonal em TODAS posições de um mundo de tamanho 8x8;

def virar_direita():
    turn_left()
    turn_left()
    turn_left()


def mover():
    move()
    put_beeper()


def diagonal_1():
    for cont in range(7):
        mover()
        turn_left()
        mover()
        virar_direita()


def diagonal_2():
    for cont in range(5):
        turn_left()
        mover()
        virar_direita()
        mover()

    turn_left()
    mover()

def diagonal_3():
    for cont in range(2):
        mover()
        virar_direita()
        mover()
        turn_left()
        mover()
        virar_direita()
        mover()
        turn_left()


def diagonal_4():
    mover()
    turn_left()
    mover()
    virar_direita()
    mover()
    turn_left()
    mover()


def diagonal_5():
    for cont in range(7):
        mover()
        virar_direita()
        mover()
        turn_left()


def iniciar_rota():
    virar()
    mover2()


def virar():
    turn_left()
    turn_left()


def mover2():
    mover()
    mover()


def main():
    diagonal_1()
    virar()
    mover2()
    diagonal_2()

    virar()
    mover2()

    diagonal_3()
    turn_left()
    mover2()

    diagonal_4()

    virar()
    mover2()

    virar_direita()

    diagonal_5()


if __name__ == "__main__":
    run_karel_program()


