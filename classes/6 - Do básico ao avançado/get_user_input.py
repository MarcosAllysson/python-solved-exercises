"""
Get data from user
"""

user_input_name = input('What is your name? ').strip().title()
print(f'\tWelcome: {user_input_name}')

user_input_age = int(input('\nHow old are you? '))
print(f'\tOk, you are {user_input_age} years old. Nice to meet ya!')
