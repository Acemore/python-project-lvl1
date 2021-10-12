from random import randint
from brain_games import rounds_count
from brain_games.brain_games_engine import run_game


def get_random_numbers():
    random_numbers = []

    [random_numbers.append(randint(0, 100)) for _ in range(rounds_count)]

    return random_numbers


def is_even(random_numbers_list):
    is_even_list = []

    for i in range(rounds_count):
        if random_numbers_list[i] % 2 == 0:
            is_even_list.append('yes')
        else:
            is_even_list.append('no')

    return is_even_list


def play_game_even():
    game_rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    random_numbers = get_random_numbers()
    correct_answers = is_even(random_numbers)

    run_game(game_rules, random_numbers, correct_answers)
