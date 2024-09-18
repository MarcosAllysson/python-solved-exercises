"""
Exercise 1: Given two integer numbers return their product. If the product is greater than 1000, then return their sum
Given 1:
    number1 = 20
    number2 = 30
Expected Output:
    The result is 600
"""
from functools import reduce


def simple_mathematic(number_1, number_2):
    try:
        product = number_1 * number_2
        message = 'The result is'

        if product > 100:
            list_of_numbers = [number_1, number_2]
            return f'{message} {reduce(lambda a, b: a + b, list_of_numbers)}'

    except Exception as error:
        print(f'Ops, an error: {error}')

    else:
        return f'{message} {product}'


number1 = 20
number2 = 30
print(simple_mathematic(number1, number2))
