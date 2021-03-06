"""
Programacion Orientada a Objetos
autr: Jan3r
Date: 2020-06-25

"""

from lamp import Lamp


def run():
    lamp = Lamp(is_turned_on=False)
    lamp._display_image()

    while True:
        command = input('''
            ¿Qué deseas hacer?

            [p]render
            [a]pagar
            [s]alir
        ''')

        if command == 'p':
            lamp.turn_on()
        elif command == 'a':
            lamp.turn_off()
        else:
            break


if __name__ == '__main__':
    run()
