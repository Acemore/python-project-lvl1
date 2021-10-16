from random import randint
from brain_games.games import MIN_INT_ZERO_TO_RANDOM


GAME_RULES = 'What number is missing in the progression?'
MAX_PROGRESSION_ELEMENT = 19
MAX_PROGRESSION_LENGTH = 10
MAX_PROGRESSION_STEP = 12
MIN_PROGRESSION_ELEMENT = 1
MIN_PROGRESSION_LENGTH = 5
MIN_PROGRESSION_STEP = -12


correct_answer = int()


def get_question():
    progression_element = randint(
        MIN_PROGRESSION_ELEMENT,
        MAX_PROGRESSION_ELEMENT
    )
    progression_step = randint(MIN_PROGRESSION_STEP, MAX_PROGRESSION_STEP)
    progression_length = randint(MIN_PROGRESSION_LENGTH, MAX_PROGRESSION_LENGTH)

    progression = []

    for i in range(progression_length):
        progression.append(progression_element)

        if i == progression_length - 1:
            break

        progression_element += progression_step

    element_to_hide_index = randint(
        MIN_INT_ZERO_TO_RANDOM,
        len(progression) - 1
    )
    global correct_answer
    correct_answer = progression[element_to_hide_index]
    progression[element_to_hide_index] = '..'

    progression = [str(element) for element in progression]

    return ' '.join(progression)


def get_answer(question):
    return correct_answer
