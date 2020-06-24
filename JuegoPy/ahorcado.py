"""
Juego de Ahorcado
Autor: Jan3r
Date: 20-06-24
"""
import random


IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']
WORDS = [
    'LAVADORA',
    'SECADORA',
    'SOFA',
    'IMPRESORA',
    'ESTUDIANTE',
    'MATEMATICAS',

]

def random_word():
    index = random.randint(0,len(WORDS)-1)
    return  WORDS[index]

def display_board(hidden_word,tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print(('---------------------------------'))


def run():
    word = random_word()
    hidden_word = ['-']* len(word)
    tries = 0
    while True:
        display_board(hidden_word,tries)
        current_letter = input('Ingrese un letra: ')

        letter_indexes = []
        for i in range(len(word)):
            if word[i] == current_letter.upper():
                letter_indexes.append(i)
        if len(letter_indexes) == 0:
            tries += 1
            if tries == 7:
                display_board(hidden_word,tries)
                print('GameOvers')
                print('Palabra Correcta era {}'.format(word))
                break

        else:
            for idx in letter_indexes:
               hidden_word[idx] = current_letter

            letter_indexes = []
        try:
            hidden_word.index('-')
        except ValueError:
            print('Ganaste')
            print('la Palabra es {}'.format(hidden_word))
            break

if __name__ == '__main__':
    run()