numeros = [int(input('Digite um número: '))]
while True:
    n = input('\nQuer adicionar mais um número?\nSim = número / Não = qualquer letra: ')
    if n.isdigit() is False:
        print(f'\n{"* " * 15}\n{"ENCERRADO":^30}\n{"* " * 15}')
        break
    else:
        numeros.append(int(n))
print(f'\nForam digitados {len(numeros)} elementos')
print(f'Os números digitados em ordem decrescente são: {sorted(numeros, reverse=True)}')
if 5 in numeros:
    print(f'O número 5 foi digitado {numeros.count(5)} vezes sendo inserido a primeira vez na {numeros.index(5)}ª '
          f'posição')
else:
    print('Não foi digitado nenhum número 5')
