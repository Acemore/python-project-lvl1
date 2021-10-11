import prompt


def run_game(game_rules, data_in, correct_answer):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(user_name))

    print(game_rules)

    for i in range(3):
        print('Question: {}'.format(data_in[i]))
        user_answer = prompt.string('Your answer: ')

        if user_answer == str(correct_answer[i]):
            print('Correct!')
        else:
            print(
                "'{}' is wrong answer ;(. Correct answer was '{}'."
                .format(user_answer, correct_answer[i])
            )
            print("Let's try again, {}!".format(user_name))

            exit()

    print('Congratulations, {}!'.format(user_name))
