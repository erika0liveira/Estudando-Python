# Ex 86 e 87

matriz = []
aux = []
l = 0
soma = 0
col3 = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        aux.append(int(input(f'Digite um valor para [{linha}] [{coluna}]: ')))
        if len(aux) == 3:
            matriz.append(aux[:])
            aux.clear()

print('\n')
print(f'{" MATRIZ ":-^44}')

# C = auxiliar para as colunas

while l < 3:
    for c in range(len(matriz)):
        print(f'[{matriz[l][c]:^10}]', end=' ')
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
        if c == 2:
            col3 += matriz[l][c]
            print()
            l += 1
        if l == 1:
            maior = max(matriz[l])

print('-'*44)
print(f'\nA soma de todos os números pares é {soma}')
print(f'A soma dos números da terceira coluna é {col3}')
print(f'O maior valor da segunda linha é {maior}')
