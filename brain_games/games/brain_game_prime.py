from math import sqrt
from random import randint
from brain_games.games import MAX_INT_TO_RANDOM, MIN_INT_ONE_TO_RANDOM


GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question():
    return randint(MIN_INT_ONE_TO_RANDOM, MAX_INT_TO_RANDOM)


def get_answer(random_number):
    is_prime_number = True

    for i in range(1, round(sqrt(random_number)) + 1):
        if random_number == 1 or i != 1 and random_number % i == 0:
            is_prime_number = False
            break

    return 'yes' if is_prime_number else 'no'
