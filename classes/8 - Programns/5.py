"""
Exercise 5: Given a two Python list. Iterate both lists simultaneously such that list1 should display item in original
order and list2 in reverse order
Given:
    list1 = [10, 20, 30, 40]
    list2 = [100, 200, 300, 400]
Expected output:
    10 400
    20 300
    30 200
    40 100
"""


def iterate_two_lists(list1, list2):
    try:
        if len(list1) > 0 and len(list2) > 0:
            for item in range(len(min(list1, list2))):
                list2.reverse()
                print(list1[item], list2[item])

        else:
            print('\033[33mBoth lists must have at least 1 item.\033[m')

    except IndexError:
        print('\033[31mLists have different sizes.\033[m')

    except Exception as error:
        print(f'{error.__class__}, {error}')


list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
iterate_two_lists(list1, list2)
