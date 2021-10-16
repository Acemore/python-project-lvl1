import random
from brain_games.games import MAX_INT_TO_RANDOM, MIN_INT_ZERO_TO_RANDOM


GAME_RULES = 'What is the result of the expression?'
OPERATIONS_STRING = '+-*'


def get_question():
    return '{} {} {}'.format(
        random.randint(MIN_INT_ZERO_TO_RANDOM, MAX_INT_TO_RANDOM),
        random.choice(OPERATIONS_STRING),
        random.randint(MIN_INT_ZERO_TO_RANDOM, MAX_INT_TO_RANDOM)
    )


def get_answer(question):
    question = question.split(' ')

    first_operand = int(question[0])
    operation = question[1]
    second_operand = int(question[2])

    if operation == '+':
        return first_operand + second_operand
    elif operation == '-':
        return first_operand - second_operand
    else:
        return first_operand * second_operand
