def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado
    :param show: opcional para mostrar o processo de multiplicação
    :return: retorna o resultado do fatorial de n
    """
    print(f'Calculando {n}! = ', end='')
    for i in range(n - 1, 0, -1):
        n *= i
        if show:
            print(f'{i}', end='')
            print(' x ' if i > 1 else ' = ', end='')
    return n


print(fatorial(5, show=False))
print(fatorial(5, show=True))
help(fatorial)
