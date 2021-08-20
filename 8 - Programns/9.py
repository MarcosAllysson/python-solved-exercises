"""
Exercise 9: Given a Python list, find value 20 in the list, and if it is present, replace it with 200. Only update the
first occurrence of a value
Given
    list1 = [5, 10, 15, 20, 25, 50, 20]
Expected output:
    list1 = [5, 10, 15, 200, 25, 50, 20]
"""


def replace_value_list(list_original, value=0, replace_number=0):
    if len(list_original) > 0:

        list_index = list_original.index(20)
        list_original[list_index] = 200

        return list_original

    else:
        return 'Empty list can not be iterated.'


list1 = [5, 10, 15, 20, 25, 50, 20]
print(replace_value_list(list1, 20, 200))
