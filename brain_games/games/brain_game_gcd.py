from random import randint
from brain_games.games import MAX_INT_TO_RANDOM, MIN_INT_ONE_TO_RANDOM


GAME_RULES = 'Find the greatest common divisor of given numbers.'


def get_question():
    return '{} {}'.format(
        randint(MIN_INT_ONE_TO_RANDOM, MAX_INT_TO_RANDOM),
        randint(MIN_INT_ONE_TO_RANDOM, MAX_INT_TO_RANDOM)
    )


def get_answer(question):
    question = question.split(' ')

    first_random_int = int(question[0])
    second_random_int = int(question[1])

    dividend = max(first_random_int, second_random_int)
    divisor = min(first_random_int, second_random_int)

    while dividend % divisor != 0:
        remainder = dividend % divisor
        dividend = divisor
        divisor = remainder

    return divisor
