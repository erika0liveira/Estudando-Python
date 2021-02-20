from math import factorial

n = int(input('Digite um número para fazer o fatorial: '))

# Usando a biblioteca MATH
print('\nO fatorial de {} é {}'.format(n, factorial(n)))

# Usando FOR
print('Calculando {}! = {} x '.format(n, n), end='')
for i in range(n-1, 0, -1):
    print('{}'.format(i), end='')
    print(' x ' if i > 1 else ' = ', end='')
    n *= i
print('{}'.format(n))

# Usando WHILE
contador = n
fatorial = 1

print('Calculando {}! = '.format(n), end='')
while contador > 0:
    print('{}'.format(contador), end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fatorial *= contador
    contador -= 1

print(fatorial)
