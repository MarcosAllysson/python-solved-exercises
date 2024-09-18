"""
Exercise 2: Concatenate two lists index-wise
Given:
    list1 = ["M", "na", "i", "Ke"]
    list2 = ["y", "me", "s", "lly"]
Expected output:
    ['My', 'name', 'is', 'Kelly']
"""


def concatenate_two_lists(list_one=None, list_two=None):
    concatenated_list = list()

    try:
        if len(list_one) > 0 and len(list_two) > 0:
            print(f'Given: \n \tlist1 = {list_one} \n \tlist2 = {list_two}')
            for i in range(len(min(list_one, list_two))):
                concatenated_list.append(list_one[i] + list_two[i])

        else:
            print(f'{"Lists length must be greater than 0"}')

    except TypeError:
        print('Pay attention to the type.')

    except Exception as error:
        print(f'\033[31mOps, got an error: {error}\033[m')

    else:
        print(f'Expected output: \n \t{concatenated_list}')

    finally:
        print("\033[33mSee ya!\033[m")


list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

concatenate_two_lists(list1, list2)
