from stanfordkarel import *


def mover():
        move()
        if beepers_present():
            pick_beeper()


def virar_direita():
    for cont in range(3):
        turn_left()


def girar_180():
    for contador in range(2):
        turn_left()


def mover_para_fronteira():
    while front_is_clear():
        mover()


def main():

    while beepers_in_bag() ==0:
        while right_is_blocked():
            print('direita bloqueada')
            turn_left()
            mover_para_fronteira()
            if beepers_in_bag()==1:
                break


        if right_is_clear():
            print('direita limpa')
            virar_direita()
            mover()


if __name__ == '__main__':
    run_karel_program('.\maze_8x8_type_I.w')