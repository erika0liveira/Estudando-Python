numeros = {}
c = 0

for i in range (1, 7):
    numeros[i] = int(input('Digite o {}° número: '.format(i)))
    if numeros[i] % 2 == 0:
        c += numeros[i]

print('\nA soma dos números pares digitados é: {}'.format(c))

