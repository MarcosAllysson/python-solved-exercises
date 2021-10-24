"""
Exercise 5: Check if the first and last number of a list is the same
Write a function to return True if the first and last number of a given list is same. If numbers are different
then return False.
Expected Output:
    Given list: [10, 20, 30, 40, 10]
    result is True
"""


def check_first_last_number_list(user_list: list) -> bool:

    if len(user_list) > 0:

        if user_list[0] == user_list[-1]:
            return True

        return False

    return False


numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]
print(check_first_last_number_list(numbers_x))
print(check_first_last_number_list(numbers_y))
