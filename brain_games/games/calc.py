from random import randint, choice


RULE = "What is the result of the expression?"


def data():
    random_number1 = randint(0, 100)
    random_number2 = randint(0, 100)
    operations = ['+', '-', '*']
    current_operation = choice(operations)
    if current_operation == '+':
        answer = random_number1 + random_number2
    if current_operation == '-':
        answer = random_number1 - random_number2
    if current_operation == '*':
        answer = random_number1 * random_number2
    question = (f"{random_number1} {current_operation} {random_number2}")
    return question, str(answer)
