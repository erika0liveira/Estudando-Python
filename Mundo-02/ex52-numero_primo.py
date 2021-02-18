c = 0
n = int(input('Digite um número para saber se é primo: '))

for i in range(1, n+1):
    if n % i == 0:
        c += 1

if c == 2:
    print('\nO número {} foi divisível apenas por 1 e por {}, portanto é um número primo!'.format(n, n, c))
else:
    print('\nO número {} foi divisível {} vezes, portanto não é um número primo!'.format(n, c))

