#!/usr/bin/env python3

import prompt
import random
import brain_games.cli


def main():
    print(f"{'Welcome to the Brain Games!'}")
    name = brain_games.cli.welcome_user()
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")

    answer_counter = 0
    while answer_counter < 3:
        current_number = random.randint(1, 99)
        print(f'Question: {current_number}')
        current_answer = prompt.string('Your answer: ')

        if current_answer == 'no' and current_number % 2 == 0:
            print("'no' is wrong answer ;(. Correct answer was 'yes'.")
            print(f"Let's try again, {name}!")
            break
        elif current_answer == 'no' and current_number % 2 == 1:
            print("Correct!")
            answer_counter += 1
            continue
        elif current_answer == 'yes' and current_number % 2 == 1:
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {name}!")
            break
        elif current_answer == 'yes' and current_number % 2 == 0:
            print("Correct!")
            answer_counter += 1
            continue
        else:
            print(f"Answer '{current_answer}' incorrect. \
                  Must be 'yes' or 'no'.")
            break

    if answer_counter == 3:
        print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
