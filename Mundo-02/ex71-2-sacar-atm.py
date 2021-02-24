from time import sleep

print('* '*26)
print('{:^50}'.format('CAIXA ELETRÔNICO'))
print('* '*26)

valor = int(input('\nQual valor deseja sacar? R$ '))

total = valor
ced = 50
totced = 0

print('\nCalculando', end='')
sleep(0.5)
print('.', end='')
sleep(0.5)
print('.', end='')
sleep(0.5)
print('.')

while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'\nTotal de {totced} cédulas de R$ {ced:.2f}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break

print('\n')
print('* '*26)
print('{:^50}'.format('FIM DO PROGRAMA'))
print('* '*26)