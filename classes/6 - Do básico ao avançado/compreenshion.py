friends = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']

# print([friend.capitalize() for friend in friends])

pares = []
impares = []

# pares.append([num for num in range(0, 20) if num % 2 == 0])
# impares.append([num for num in range(0, 20) if num % 2 != 0])
#
# print(f'Pares: {pares}\nÍmpares: {impares}')


aninhada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([lista for lista in aninhada])
