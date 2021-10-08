"""
Exercise 2: Given a range of the first 10 numbers, Iterate from the start number to the end number, and In each
iteration print the sum of the current number and previous number
    Printing current and previous number sum in a range(10)
    Current Number 0 Previous Number  0  Sum:  0
    Current Number 1 Previous Number  0  Sum:  1
    Current Number 2 Previous Number  1  Sum:  3
    ...
"""

for i in range(10):
    if i == 0:
        print(f'Current Number {i} Previous Number {i} Sum: {i + i}')

    else:
        print(f'Current Number {i} Previous Number {i-1} Sum: {i + i - 1}')
