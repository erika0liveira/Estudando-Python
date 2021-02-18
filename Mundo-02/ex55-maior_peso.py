menor = 0
maior = 0
m = 0

for i in range(1, 6):
    pesos = float(input('Digite o peso em KG da {}° pessoa: '.format(i)))
    m += pesos
    if i == 1:
        menor = pesos
        maior = pesos
    else:
        if pesos < menor:
            menor = pesos
        if pesos > maior:
            maior = pesos

print('\nO menor peso foi: {} Kg '.format(menor))
print('O maior peso foi: {} Kg '.format(maior))

print('\nA média dos pesos informados foi de: {:.1f} Kg'.format(m/5))

