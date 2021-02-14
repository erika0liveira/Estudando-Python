a = float(input('Digite o tamanho da 1° reta: '))
b = float(input('Digite o tamanho da 2° reta: '))
c = float(input('Digite o tamanho da 3° reta: '))

if (a + b) > c and (b + c) > a and (a + c) > b:
    print('\nCom os valores informados {:.2f}, {:.2f} e {:.2f} é possível criar um triângulo'.format(a, b, c))
else:
    print('\nCom os valores informados {:.2f}, {:.2f} e {:.2f} não é possível criar um triângulo'.format(a, b, c))
