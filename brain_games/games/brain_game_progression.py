from random import randint
from brain_games import rounds_count
from brain_games.brain_games_engine import run_game


def get_progressions():
    progressions = []

    for _ in range(rounds_count):
        progression_element = randint(1, 19)
        progression_step = randint(-12, 12)
        progression_length = randint(5, 10)

        progression = []

        for i in range(progression_length):
            progression.append(progression_element)

            if i == progression_length - 1:
                break

            progression_element += progression_step

        progressions.append(progression)

    return progressions


def get_progressions_strings_and_correct_answers(progressions):
    progressions_strings_and_correct_answers = []

    for i in range(rounds_count):
        progression = progressions[i]

        element_to_hide_index = randint(0, len(progression) - 1)

        correct_answer = progression[element_to_hide_index]
        progression[element_to_hide_index] = '..'

        progression = [str(element) for element in progression]
        progression_string = ' '.join(progression)

        progressions_strings_and_correct_answers.append(
            (progression_string, correct_answer)
        )

    return progressions_strings_and_correct_answers


def play_game_progression():
    game_rules = 'What number is missing in the progression?'
    progressions_strings_and_correct_answers = (
        get_progressions_strings_and_correct_answers(get_progressions())
    )
    progressions = []
    correct_answers = []

    for i in range(rounds_count):
        progression_string, correct_answer = (
            progressions_strings_and_correct_answers[i]
        )

        progressions.append(progression_string)
        correct_answers.append(correct_answer)

    run_game(game_rules, progressions, correct_answers)
