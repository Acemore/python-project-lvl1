import prompt


ROUND_COUNT = 3


def run_game(game):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(user_name))

    print(game.GAME_RULES)

    for _ in range(ROUND_COUNT):
        question = game.get_question()
        correct_answer = str(game.get_answer(question))

        print('Question: {}'.format(question))
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(
                "'{}' is wrong answer ;(. Correct answer was '{}'."
                .format(user_answer, correct_answer)
            )
            print("Let's try again, {}!".format(user_name))

            exit()

    print('Congratulations, {}!'.format(user_name))
