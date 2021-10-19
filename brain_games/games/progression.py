from random import randint
from brain_games.games import MIN_INT_ZERO_TO_RANDOM


MAX_PROGRESSION_COMMON_DIFFERENCE = 12
MAX_PROGRESSION_LENGTH = 10
MAX_PROGRESSION_TERM = 19
MIN_PROGRESSION_COMMON_DIFFERENCE = -12
MIN_PROGRESSION_LENGTH = 5
MIN_PROGRESSION_TERM = 1
RULES = 'What number is missing in the progression?'


def calculate_progression_terms():
    progression_term = randint(
        MIN_PROGRESSION_TERM,
        MAX_PROGRESSION_TERM
    )
    progression_common_difference = randint(
        MIN_PROGRESSION_COMMON_DIFFERENCE,
        MAX_PROGRESSION_COMMON_DIFFERENCE
    )
    progression_length = randint(MIN_PROGRESSION_LENGTH, MAX_PROGRESSION_LENGTH)

    progression = []

    for i in range(progression_length):
        progression.append(progression_term)

        if i == progression_length - 1:
            break

        progression_term += progression_common_difference

    return progression


def get_progression_string(progression, term_to_hide_index):
    progression[term_to_hide_index] = '..'

    progression = [str(term) for term in progression]

    return ' '.join(progression)


def get_question_and_answer():
    progression = calculate_progression_terms()
    term_to_hide_index = randint(
        MIN_INT_ZERO_TO_RANDOM,
        len(progression) - 1
    )

    answer = progression[term_to_hide_index]
    question = get_progression_string(progression, term_to_hide_index)

    return (question, answer)
