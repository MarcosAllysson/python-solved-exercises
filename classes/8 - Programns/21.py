"""
Exercise 9: Check Palindrome Number
Write a program to check if the given number is a palindrome number.
A palindrome number is a number that is same after reverse. For example 545, is the palindrome numbers
Expected Output:
    original number 121
    Yes. given number is palindrome number
"""


def check_palindrome_number(number: int) -> bool:
    original_number = number
    
    reverse_num = 0
    while number > 0:
        reminder = number % 10
        reverse_num = (reverse_num * 10) + reminder
        number = number // 10

    if original_number == reverse_num:
        return True
    
    return False

print(check_palindrome_number(545))
print(check_palindrome_number(546))