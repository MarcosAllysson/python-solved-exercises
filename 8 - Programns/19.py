"""
Exercise 7: Return the count of a given substring from a string
Write a program to find how many times substring “Emma” appears in the given string.
Given:
    str_x = "Emma is good developer. Emma is a writer"
Expected Output:
    Emma appeared 2 times
"""

from collections import Counter


def count_string(string: str) -> str:
    user_string = Counter(string.strip().split())

    if user_string.get('Emma', 0) > 0:
        return f'Emma appeared {user_string["Emma"]} times.'

    return f'Emma appeared not even once.'


str_x = "Emma is good developer. Emma is a writer"
print(count_string(string=str_x))
