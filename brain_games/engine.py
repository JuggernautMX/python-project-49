import prompt


ANSWERS_REQUIRED = 3


def engine(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(f'{game.RULE}')
    answers_given = 0

    while answers_given < ANSWERS_REQUIRED:
        question, answer = game.data()
        print('Question: ' + question)
        current_answer = prompt.string('Your answer: ')

        if current_answer == answer:
            print('Correct!')
            answers_given += 1
        else:
            print(
                f"'{current_answer}' is wrong answer ;(. "
                f"Correct answer was '{answer}'.\n"
                f"Let\'s try again, {name}!"
            )
            break
    else:
        print(f'Congratulations, {name}!')
