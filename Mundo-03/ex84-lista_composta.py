from time import sleep

p = []
pessoas = []
pesos = []
c = ''

while True:
    print(f'\n{"-" * 50}')
    p.append(str(input('Digite o nome: ')))
    p.append(float(input('Digite o peso: ')))
    print('-' * 50)

    pessoas.append(p[:])
    p.clear()

    c = str(input('\nQuer continuar? [S/N]: ')).lower()[0]

    if c == 'n':
        print('\nAnalisando', end='')
        sleep(0.5)
        print('.', end='')
        sleep(0.5)
        print('.', end='')
        sleep(0.5)
        print('.')
        break

for i in pessoas:
    if i[1] not in pesos:
        pesos.append(i[1])

print(f'\nO total de pessoas cadastradas foram: {len(pessoas)}')

maior = max(pesos)
print(f'\nO maior peso foi de: {maior} kg. Peso da(s) pessoa(s) abaixo: ')
for j in pessoas:
    if j[1] == maior:
        print(j[0])

menor = min(pesos)
print(f'\nO menor peso foi de: {menor} kg. Peso da(s) pessoa(s) abaixo: ')
for k in pessoas:
    if k[1] == menor:
        print(k[0])
