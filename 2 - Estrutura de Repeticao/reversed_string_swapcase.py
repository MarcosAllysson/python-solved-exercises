def reverse_words_order_and_swap_cases(sentence):
    """
    PYTHON REVERSE WORDS ORDER AND SWAP CASES
    Complete the 'reverse_words_order_and_swap_cases' function below.
    The function is expected to return a STRING.
    The function accepts STRING sentence as parameter.
    """

    # Tirando espaços da string e quebrando no espaço
    reverse = sentence.strip().split()

    # formando lista reversa
    reverse = list(reversed(reverse))

    # usando join e retornando a nova string
    new_string = " ".join(reverse).swapcase()
    return new_string


if __name__ == '__main__':
    sentence = str(input('Insira uma string: '))
    result = reverse_words_order_and_swap_cases(sentence)
    print(result)
