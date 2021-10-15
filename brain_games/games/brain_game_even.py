from random import randint


GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question():
    return randint(0, 100)


def get_answer(random_number):
    return 'yes' if random_number % 2 == 0 else 'no'
