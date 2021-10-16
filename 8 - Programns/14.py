"""
Exercise 3: Print characters from a string that are present at an even index number
Write a program to accept a string from the user and display characters that are present at an even index number.
    For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.
"""


def print_string_even_index_number(user_string: str = '') -> list:
    user_string_formatted = user_string.strip().lower()
    user_string_list = []

    for index, letter in enumerate(user_string_formatted):
        if index % 2 == 0:
            user_string_list.append(letter)

    return user_string_list


print(print_string_even_index_number('pynative'))
