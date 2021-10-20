from random import randint


MAX_INT_TO_RANDOM = 100
MIN_INT_ZERO_TO_RANDOM = 0
MIN_INT_ONE_TO_RANDOM = 1


def get_parameters_for_question_and_answer(
    min_int_to_random, max_int_to_random, predicate
):
    question = randint(min_int_to_random, max_int_to_random)
    answer = 'yes' if predicate(question) else 'no'

    return question, answer
