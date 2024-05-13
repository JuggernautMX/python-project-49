import math
from random import randint


RULE = 'Find the greatest common divisor of given numbers.'


def data():
    random_number1 = randint(10, 100)
    random_number2 = randint(10, 100)
    question = f'{random_number1} {random_number2}'
    answer = math.gcd(random_number1, random_number2)
    return question, str(answer)
