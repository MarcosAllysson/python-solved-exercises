"""
Exercise 6: Display numbers divisible by 5 from a list
Iterate the given list of numbers and print only those numbers which are divisible by 5
Expected Output:
    Given list is  [10, 20, 33, 46, 55]
    Divisible by 5: 10, 20, 55
"""


def check_numbers_divisible_by_five(user_list: list) -> list:

    if len(user_list) > 0:
        try:
            filtered_list = list(filter(lambda number: number % 5 == 0, user_list))

            if filtered_list:
                return filtered_list

        except TypeError:
            return []

    return []


user_list = [10, 20, 33, 46, 55]
print(check_numbers_divisible_by_five(user_list=user_list))
