"""
Exercise 8: Print the following pattern
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""


def pattern(number: int):

    try:
        if number > 0:
            for i in range(number + 1):
                print(f'{" ".join(i * str(i))}')

    except TypeError:
        print('Only number higher than 0 is allowed.')

    except ValueError:
        print('Only digits are allowed!')

    except:
        print('Try again sending a valid number.')


pattern(number=6)
