#Exercício Mundo-01/03-Condições/EX-26 implementado

import sys

a = float(input('Digite o tamanho da 1° reta: '))
b = float(input('Digite o tamanho da 2° reta: '))
c = float(input('Digite o tamanho da 3° reta: '))

if (a + b) > c and (b + c) > a and (a + c) > b:
    print('\nCom os valores informados {:.1f}, {:.1f} e {:.1f} é possível criar um triângulo '.format(a, b, c), end='')
    if a == b == c:
       print('Equilátero')
    elif a != b != c != a:
        print('Escaleno')
    else:
        print('Isósceles')
else:
    print('\nCom os valores informados {:.2f}, {:.2f} e {:.2f} não é possível criar um triângulo'.format(a, b, c))
    sys.exit()



