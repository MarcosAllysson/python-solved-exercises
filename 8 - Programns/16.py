"""
Exercise 5: Check if the first and last number of a list is the same
Write a function to return True if the first and last number of a given list is same. If numbers are different then
return False.
Given: numbers_x = [10, 20, 30, 40, 10]
Expected Output: result is True
"""


def check_list_number(user_list: list) -> bool:

    if len(user_list) > 0:
        if user_list[0] == user_list[-1]:
            return True

        else:
            return False

    return False


try:
    user_list = []

    while True:
        temp_number = int(input('Number ou "0" to stop and analyze: '))

        if temp_number != 0:
            user_list.append(temp_number)

        else:
            break

    print(check_list_number(user_list=user_list))

except ValueError:
    print(f'Insert only numbers different than 0.')
