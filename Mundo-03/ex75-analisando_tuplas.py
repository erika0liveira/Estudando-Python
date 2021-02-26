nlista = []
par = []

for i in range(4):
    i = int(input(f'Digite o {i+1}° número: '))
    nlista.append(i)

    if i % 2 == 0:
        par.append(i)

nTupla = tuple(nlista)

print(f'\nVocê digitou os números: {nTupla}')

if 9 in nTupla:
    print(f'O número 9 apareceu {nTupla.count(9)} vezes')
else:
    print('Você não digitou nenhum número 9')

if 3 in nTupla:
    print(f'O número 3 aparece a primeira vez na {nTupla.index(3)+1}ª posição')
else:
    print('Não foi digitado nenhum número 3')

print(f'Os números pares digitados foram: {par}')
