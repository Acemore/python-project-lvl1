import prompt

def run_game(game_descrition, data_in, correct_answer):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    
    print(game_descrition)

    for _ in range(3):
        print('Question: {}'.format(data_in))
        user_input = prompt.string('Your answer: ')
        
        if user_input == str(correct_answer):
            print('Correct!')
        else:
            print('{} is wrong answer ;(. Correct answer was {}.'.format(user_input, correct_answer))
            break

    print('Congratulations, {}!'.format(name))