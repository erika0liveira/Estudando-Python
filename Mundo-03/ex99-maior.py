from time import sleep

print('-' * 50)


def maior(*n):
    if max(n) == 0:
        print(f'Analisando os 0 valores informados: ', end=' ')
    else:
        print(f'Analisando os {len(n)} valores informados: ', end=' ')
    for i in n:
        sleep(0.5)
        print(i, end=' ')
    print(f'\nO maior valor informado foi: {max(n)}')
    print('-' * 50)


maior(1, 2, 3, 4, 5, 6)
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)
