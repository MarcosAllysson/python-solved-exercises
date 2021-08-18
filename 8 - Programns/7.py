"""
Exercise 7: Add item 7000 after 6000 in the following Python List
Given:
    list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
Expected output:
    [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
"""


def add_item_list(list_original, item):
    list_original[2][2].insert(2, item)

    return list_original


list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
print(add_item_list(list1, 700))
