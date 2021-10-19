from math import sqrt
from random import randint
from brain_games.games import MAX_INT_TO_RANDOM, MIN_INT_ONE_TO_RANDOM


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    is_prime_number = True

    for i in range(1, round(sqrt(number)) + 1):
        if number == 1 or i != 1 and number % i == 0:
            is_prime_number = False
            break

    return 'yes' if is_prime_number else 'no'


def get_question_and_answer():
    question = randint(MIN_INT_ONE_TO_RANDOM, MAX_INT_TO_RANDOM)
    answer = is_prime(question)

    return (question, answer)
