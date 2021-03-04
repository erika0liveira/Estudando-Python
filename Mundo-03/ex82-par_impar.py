completo = [int(input('Digite um número: '))]
par = []
impar = []
while True:
    n = input('\nQuer adicionar mais um número?\nSim = número / Não = qualquer letra: ')
    if n.isdigit() is False:
        print(f'\n{"* " * 15}\n{"ENCERRADO":^30}\n{"* " * 15}')
        break
    else:
        completo.append(int(n))
for i in range(len(completo)):
    if completo[i] % 2 == 0:
        par.append(completo[i])
    else:
        impar.append(completo[i])
print(f'\nOs números digitados foram: {sorted(completo)}')
if not par:
    print('Não foi digitado nenhum número par')
else:
    print(f'Os números pares são: {sorted(par)}')
if not impar:
    print('Não foi digitado nenhum número ímpar')
else:
    print(f'Os números ímpares são: {sorted(impar)}')
