from random import randint
from brain_games import rounds_count
from brain_games.brain_games_engine import run_game


def get_random_ints():
    random_ints = []

    for _ in range(rounds_count):
        first_random_int = randint(1, 100)
        second_random_int = randint(1, 100)

        random_ints.append((first_random_int, second_random_int))

    return random_ints


def make_random_ints_strings(random_ints):
    random_ints_pairs = []

    for i in range(rounds_count):
        first_random_int, second_random_int = random_ints[i]

        random_ints_pairs.append(
            '{} {}'
            .format(first_random_int, second_random_int)
        )

    return random_ints_pairs


def find_gcd(random_ints):
    correct_answers = []

    for i in range(rounds_count):
        first_random_int, second_random_int = random_ints[i]

        dividend = max(first_random_int, second_random_int)
        divisor = min(first_random_int, second_random_int)

        while dividend % divisor != 0:
            remainder = dividend % divisor
            dividend = divisor
            divisor = remainder

        correct_answers.append(divisor)

    return correct_answers


def play_game_gcd():
    game_rules = 'Find the greatest common divisor of given numbers.'
    random_ints = get_random_ints()
    random_ints_pairs = make_random_ints_strings(random_ints)
    correct_answers = find_gcd(random_ints)

    run_game(game_rules, random_ints_pairs, correct_answers)
