from random import randint
from brain_games.games import MAX_INT_TO_RANDOM, MIN_INT_ONE_TO_RANDOM


RULES = 'Find the greatest common divisor of given numbers.'


def find_gcd(first_number, second_number):
    dividend = max(first_number, second_number)
    divisor = min(first_number, second_number)

    while dividend % divisor != 0:
        remainder = dividend % divisor
        dividend = divisor
        divisor = remainder

    return divisor


def get_question_and_answer():
    first_random_int = randint(MIN_INT_ONE_TO_RANDOM, MAX_INT_TO_RANDOM)
    second_random_int = randint(MIN_INT_ONE_TO_RANDOM, MAX_INT_TO_RANDOM)

    question = '{} {}'.format(first_random_int, second_random_int)

    answer = find_gcd(first_random_int, second_random_int)

    return (question, answer)
