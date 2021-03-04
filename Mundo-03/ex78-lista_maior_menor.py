numeros = []

for i in range(5):
    numeros.append(int(input(f'Digite o {i+1}º número: ')))
menor = min(numeros)
maior = max(numeros)

print(f'\nOs valores digitados foram: {numeros}')

print(f'\nO menor valor foi: {menor} que está nas posições: ', end='')
for n in range(5):
    if numeros[n] == menor:
        print(f'{n + 1}', end='... ')

print(f'\nO maior valor foi: {max(numeros)} que está nas posições: ', end='')
for m in range(5):
    if numeros[m] == maior:
        print(f'{m + 1}', end='... ')
