from random import randint
from brain_games.games import MAX_INT_TO_RANDOM, MIN_INT_ZERO_TO_RANDOM


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def get_question_and_answer():
    question = randint(MIN_INT_ZERO_TO_RANDOM, MAX_INT_TO_RANDOM)
    answer = 'yes' if is_even(question) else 'no'

    return question, answer
