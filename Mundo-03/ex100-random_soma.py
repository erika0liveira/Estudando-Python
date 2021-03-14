from random import randint


def valores(lst):
    print('Sorteando os valores: ', end='')
    for i in range(0, 5):
        lst.append(randint(0, 20))
        print(lst[i], end=' ')
    print()


def somaPar(lst):
    print(f'Somando os valores pares em {lst} temos: ', end='')
    soma = 0
    for i in lst:
        if i % 2 == 0:
            soma += i
    print(soma)


lstrand = []

valores(lstrand)
somaPar(lstrand)
