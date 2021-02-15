a = float(input('Informe sua altura: '))
p = float(input('Informe seu peso: '))

imc = p / (a ** 2)

print('\nSeu ICM é de: {:.1f}'.format(imc))

if imc < 18.5:
    print('\nVocê está \033[1;31mabaixo do peso ideal\033[m')
elif imc < 25:
    print('\nVocê está \033[1;32mpeso ideal\033[m')
elif imc < 30:
    print('\nVocê está com \033[1;31msobrepeso\033[m')
elif imc < 40:
    print('\nVocê está \033[1;31mobeso\033[m')
else:
    print('\nVocê está com \033[1;31mobesidade mórbida\033[m')