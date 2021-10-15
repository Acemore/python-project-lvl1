import random


GAME_RULES = 'What is the result of the expression?'


def get_question():
    return '{} {} {}'.format(
        random.randint(0, 100),
        random.choice('+-*'),
        random.randint(1, 101)
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
