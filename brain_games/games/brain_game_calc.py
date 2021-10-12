import random
from brain_games import rounds_count
from brain_games.brain_games_engine import run_game


def get_operands_and_operations():
    operands_and_operations = []

    for _ in range(rounds_count):
        first_operand = random.randint(0, 100)
        second_operand = random.randint(1, 101)
        operation = random.choice('+-*')

        operands_and_operations.append(
            (first_operand, second_operand, operation)
        )

    return operands_and_operations


def make_math_expressions_strings(operands_and_operations):
    math_expressions = []

    for i in range(rounds_count):
        first_operand, second_operand, operation = operands_and_operations[i]

        math_expressions.append(
            '{} {} {}'
            .format(first_operand, operation, second_operand)
        )

    return math_expressions


def calculate_math_expressions(operands_and_operators):
    expressions_results = []

    for i in range(rounds_count):
        first_operand, second_operand, operation = operands_and_operators[i]

        if operation == '+':
            expressions_results.append(first_operand + second_operand)
        elif operation == '-':
            expressions_results.append(first_operand - second_operand)
        else:
            expressions_results.append(first_operand * second_operand)

    return expressions_results


def play_game_calc():
    game_rules = 'What is the result of the expression?'
    operands_and_operations = get_operands_and_operations()
    math_expressions = make_math_expressions_strings(operands_and_operations)
    correct_answers = calculate_math_expressions(operands_and_operations)

    run_game(game_rules, math_expressions, correct_answers)
