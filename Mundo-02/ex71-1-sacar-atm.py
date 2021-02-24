from time import sleep

auxiliar = 0
contador = 0

print('* '*26)
print('{:^50}'.format('CAIXA ELETRÔNICO'))
print('* '*26)

valor = int(input('\nQual valor deseja sacar? R$ '))

print('\nCalculando', end='')
sleep(0.5)
print('.', end='')
sleep(0.5)
print('.', end='')
sleep(0.5)
print('.')

print(f'\nPara sacar {valor:.2f}, serão necessárias as seguintes cédulas: ', end='\n\n')

while valor > 0:
    if valor >= 50:
        auxiliar = valor // 50
        valor = valor - (auxiliar * 50)
        contador = auxiliar

        print(f'{contador} de R$ 50,00', end='\n')

    elif valor >= 20:
        auxiliar = valor // 20
        valor = valor - (auxiliar * 20)
        contador = auxiliar

        print(f'{contador} de R$ 20,00', end='\n')

    elif valor >= 10:
        auxiliar = valor // 10
        valor = valor - (auxiliar * 10)
        contador = auxiliar

        print(f'{contador} de R$ 10,00', end='\n')

    elif valor >= 1:
        auxiliar = valor // 1
        valor = valor - (auxiliar * 1)
        contador = auxiliar

        print(f'{contador} de R$ 1,00', end='\n')
