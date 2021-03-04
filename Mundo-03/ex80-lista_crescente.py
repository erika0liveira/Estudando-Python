numeros = []
for i in range(0, 5):
    n = int(input('\nDigite um número: '))
    if i == 0 or n > numeros[-1]:
        numeros.append(n)
        print(f'Número alocado na última posição')
    else:
        p = 0
        while p < len(numeros):
            if n <= numeros[p]:
                numeros.insert(p, n)
                print(f'Número alocado na {p+1}ª posição')
                break
            p += 1
print(f'\nOs números digitados foram: {numeros}')
