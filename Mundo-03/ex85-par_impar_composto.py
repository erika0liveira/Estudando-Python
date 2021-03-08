numeros = [[], []]

for i in range(1, 8):
    n = int(input(f'Digite o {i}° número: '))

    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)

print(f'\nOs números pares foram {sorted(numeros[0])}')
print(f'Os números ímpares foram {sorted(numeros[1])}')
