"""
Exercise 3: Given a Python list of numbers. Turn every item of a list into its square
Given:
    aList = [1, 2, 3, 4, 5, 6, 7]
Expected output:
    [1, 4, 9, 16, 25, 36, 49]
"""


def square(list_itens):
    try:
        print(f'Given: \n \taList = {list_itens}')

        list_square = list(map(lambda a: a ** 2, list_itens))
        print(f'Expected output: \n \t{list_square}')

    except Exception as error:
        print(error)


aList = [1, 2, 3, 4, 5, 6, 7]
square(aList)
