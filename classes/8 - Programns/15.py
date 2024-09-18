"""
Exercise 4: Remove first n characters from a string
Write a program to remove characters from a string starting from zero up to n and return a new string.
For example:
    remove_chars("pynative", 4) so output must be tive. Here we need to remove first four characters from a string.
"""


def remove_characters(user_string: str, remove_characters_quantity: int) -> str:
    lenght_user_string = len(user_string)

    if remove_characters_quantity <= lenght_user_string:
        return f'Removing {remove_characters_quantity} characters from "{user_string}", got: ' \
               f'{user_string[remove_characters_quantity:]}'

    return 'Quantity of characters to remove is higher than string length.'


try:
    user_string = str(input('Enter a word: ')).strip()
    characters_quantity_to_remove = int(input(f'How many characters do you want to remove from "{user_string}"? '
                                              f'\nAnswer: '))

    print(remove_characters(user_string, characters_quantity_to_remove))

except ValueError:
    print('Enter only a number.')
