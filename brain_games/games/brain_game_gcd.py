from random import randint


GAME_RULES = 'Find the greatest common divisor of given numbers.'


def get_question():
    return '{} {}'.format(randint(1, 100), randint(1, 100))


def get_answer(question):
    question = question.split(' ')

    first_random_int = int(question[0])
    second_random_int = int(question[1])

    dividend = max(first_random_int, second_random_int)
    divisor = min(first_random_int, second_random_int)

    while dividend % divisor != 0:
        remainder = dividend % divisor
        dividend = divisor
        divisor = remainder

    return divisor
