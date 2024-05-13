from random import randint


RULE = "Answer 'yes' if given number is prime. Otherwise answer 'no'."


def is_prime(number):
    if number > 1:
        i = 2
        while number % i != 0 and i ** 2 <= number:
            i += 1
        if i ** 2 > number:
            return True
        else:
            return False
    else:
        return False


def data():
    random_number = randint(0, 1000)
    question = f'{random_number}'

    answer = "yes" if is_prime(random_number) else "no"

    return question, answer
