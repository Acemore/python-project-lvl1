import random
from brain_games.games import MAX_INT_TO_RANDOM, MIN_INT_ZERO_TO_RANDOM


OPERATIONS_STRING = '+-*'
RULES = 'What is the result of the expression?'


def get_question_and_answer():
    first_operand = random.randint(MIN_INT_ZERO_TO_RANDOM, MAX_INT_TO_RANDOM)
    second_operand = random.randint(MIN_INT_ZERO_TO_RANDOM, MAX_INT_TO_RANDOM)
    operation = random.choice(OPERATIONS_STRING)

    question = '{} {} {}'.format(first_operand, operation, second_operand)

    if operation == '+':
        answer = first_operand + second_operand
    elif operation == '-':
        answer = first_operand - second_operand
    else:
        answer = first_operand * second_operand

    return (question, answer)
