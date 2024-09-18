"""
Exercise 6: Remove empty strings from the list of strings
Give:
    list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
Expected output:
    ["Mike", "Emma", "Kelly", "Brad"]
"""


def remove_empty_string(list_string):
    new_string = []

    for item in list_string:
        if not item == '':
            new_string.append(item)

    return new_string


list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
print(remove_empty_string(list1))
