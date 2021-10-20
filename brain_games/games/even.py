from brain_games.games import (
    MAX_INT_TO_RANDOM,
    MIN_INT_ZERO_TO_RANDOM,
    get_parameters_for_question_and_answer
)

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def get_question_and_answer():
    return get_parameters_for_question_and_answer(
        MIN_INT_ZERO_TO_RANDOM, MAX_INT_TO_RANDOM, is_even
    )
