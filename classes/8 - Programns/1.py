"""
Exercise 1: Reverse a given list in Python
Given:
    aLsit = [100, 200, 300, 400, 500]
Expected output:
    [500, 400, 300, 200, 100]
"""


def reverse_list(list_itens):
    list_itens.reverse()
    return list_itens


aLsit = [100, 200, 300, 400, 500]
print(reverse_list(aLsit))
