"""
Exercise 10: Given a Python list, remove all occurrence of 20 from the list
Given:
    list1 = [5, 20, 15, 20, 25, 50, 20]
Expected output:
    [5, 15, 25, 50]
"""


def remove_occurrence(original_list, item):

    if len(original_list) > 0:
        for i in original_list:
            if i == item:
                original_list.remove(i)

    return original_list


list1 = [5, 20, 15, 20, 25, 50, 20]
print(remove_occurrence(list1, 20))
