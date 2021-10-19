from random import randint
from brain_games.games import MAX_INT_TO_RANDOM, MIN_INT_ZERO_TO_RANDOM


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return 'yes' if number % 2 == 0 else 'no'


def get_question_and_answer():
    question = randint(MIN_INT_ZERO_TO_RANDOM, MAX_INT_TO_RANDOM)
    answer = is_even(question)

    return (question, answer)
