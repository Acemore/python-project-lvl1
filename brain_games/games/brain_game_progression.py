from random import randint


GAME_RULES = 'What number is missing in the progression?'
correct_answer = ''


def get_question():
    progression_element = randint(1, 19)
    progression_step = randint(-12, 12)
    progression_length = randint(5, 10)

    progression = []

    for i in range(progression_length):
        progression.append(progression_element)

        if i == progression_length - 1:
            break

        progression_element += progression_step

    element_to_hide_index = randint(0, len(progression) - 1)
    global correct_answer
    correct_answer = progression[element_to_hide_index]
    progression[element_to_hide_index] = '..'

    progression = [str(element) for element in progression]

    return ' '.join(progression)


def get_answer(question):
    return correct_answer
