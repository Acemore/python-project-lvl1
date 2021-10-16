from random import randint
from brain_games.games import MAX_INT_TO_RANDOM, MIN_INT_ZERO_TO_RANDOM


GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question():
    return randint(MIN_INT_ZERO_TO_RANDOM, MAX_INT_TO_RANDOM)


def get_answer(random_number):
    return 'yes' if random_number % 2 == 0 else 'no'
