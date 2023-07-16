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
    virar()
    mover2()

def diagonal_2():
    for cont in range(5):
        turn_left()
        mover()
        virar_direita()
        mover()

    turn_left()
    mover()
    virar()
    mover2()

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
    turn_left()
    mover2()

def diagonal_4():
    mover()
    turn_left()
    mover()
    virar_direita()
    mover()
    turn_left()
    mover()
    virar()
    mover2()
    virar_direita()

def diagonal_5():
    for cont in range(7):
        mover()
        virar_direita()
        mover()
        turn_left()
    virar()
    mover2()
    virar_direita()

def diagonal_6():
    for cont in range(5):
        mover()
        turn_left()
        mover()
        virar_direita()


def diagonal_7():
    for cont in range(3):
        mover()
        virar_direita()
        mover()
        turn_left()
    mover()
    virar()
    mover2()
    turn_left()

def diagonal_8():
    for cont in range(2):
        mover()
        turn_left()
        mover()
        virar_direita()
    mover()


def diagonal_9():
    turn_left()
    mover()

    for cont in range(4):
        turn_left()
        mover()
        virar_direita()
        mover()
    virar_direita()


def diagonal_10():
    mover2()
    virar_direita()

    for cont in range(2):
        mover()
        turn_left()
        mover()
        virar_direita()
    mover()


def diagonal_final():
    virar_direita()
    for cont in range(4):
        mover()
        turn_left()
        mover()
        virar_direita()
    mover()

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


    put_beeper()
    diagonal_1()

    diagonal_2()

    diagonal_3()

    diagonal_4()

    diagonal_5()

    diagonal_6()

    diagonal_7()

    diagonal_8()

    diagonal_9()

    diagonal_10()

    diagonal_final()


if __name__ == "__main__":
    run_karel_program()


