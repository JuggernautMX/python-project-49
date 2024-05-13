from random import randint


RULE = 'What number is missing in the progression?'


def data():
    random_number = randint(0, 100)
    progression_step = randint(1, 10)
    progression_length = randint(5, 10)
    arithmetic_progression = []
    i = 0

    while i < progression_length:
        arithmetic_progression.append(
            random_number + progression_step * i
        )
        i += 1

    hidden_element = randint(0, progression_length - 1)
    answer = arithmetic_progression[hidden_element]
    arithmetic_progression[hidden_element] = '..'
    question = ' '.join(str(x) for x in arithmetic_progression)
    return question, str(answer)
