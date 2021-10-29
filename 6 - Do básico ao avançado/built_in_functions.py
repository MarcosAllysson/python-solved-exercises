from functools import reduce

numbers = [number for number in range(0, 24)]
average_numbers = lambda numbers: reduce(lambda x, y: x + y, numbers) / len(numbers)
print(f'Average of numbers: {average_numbers(numbers):.2f}')

higher_than_average = lambda numbers: list(filter(lambda x: x > average_numbers(numbers), numbers))
print(f'Numbers higher than average: {higher_than_average(numbers)}')

square_numbers = lambda numbers: list(map(lambda x: x ** 2, numbers))
print(f'Square of numbers: {square_numbers(numbers)}')

print(f'Max number: {max(numbers)}')
print(f'Min number: {min(numbers)}')
print(f'Sum of numbers: {sum(numbers)}')
print(f'Sum of numbers with reduce function: {reduce(lambda x, y: x + y, numbers)}')

numbers.sort(reverse=True)
print(f'Sorted numbers: {numbers}')
print(f'Len of numbers: {len(numbers)} digits.')
print(f'Are all numbers higher than 0? {all(numbers)}')
print(f'At least one number is 0? {any(numbers)}')
