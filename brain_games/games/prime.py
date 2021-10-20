from math import sqrt
from brain_games.games import (
    MAX_INT_TO_RANDOM,
    MIN_INT_ONE_TO_RANDOM,
    get_parameters_for_question_and_answer
)

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    is_prime_number = True

    if number == 1:
        is_prime_number = False

    for i in range(2, round(sqrt(number)) + 1):
        if number % i == 0:
            is_prime_number = False
            break

    return is_prime_number


def get_question_and_answer():
    return get_parameters_for_question_and_answer(
        MIN_INT_ONE_TO_RANDOM, MAX_INT_TO_RANDOM, is_prime
    )
