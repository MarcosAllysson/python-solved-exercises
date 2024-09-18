"""
Exercise 4: Concatenate two lists in the following order
    list1 = ["Hello ", "take "]
    list2 = ["Dear", "Sir"]
Expected output:
    ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
"""


def concatenate_two_lists(list_one, list_two):
    new_list = []

    try:
        for i in range(len(list_one)):
            for j in range(len(list_two)):
                new_list.append(list_one[i] + list_two[j])

        print(new_list)

    except Exception as error:
        print(f'An error occur, try again: {error}')


list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
concatenate_two_lists(list1, list2)
