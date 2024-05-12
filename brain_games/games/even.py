from random import randint


RULE = "Answer 'yes' if the number is even, otherwise answer 'no'."


def data():
    random_number = randint(0, 100)
    question = f"{random_number}"
    if random_number == 0:
        answer = "no"
    answer = "yes" if random_number % 2 == 0 else "no"
    return question, str(answer)
