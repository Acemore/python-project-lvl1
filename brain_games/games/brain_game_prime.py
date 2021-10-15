from math import sqrt
from random import randint


GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question():
    return randint(1, 100)


def get_answer(random_number):
    is_prime_number = True

    for i in range(1, round(sqrt(random_number)) + 1):
        if random_number == 1 or i != 1 and random_number % i == 0:
            is_prime_number = False
            break

    return 'yes' if is_prime_number else 'no'
