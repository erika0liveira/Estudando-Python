from datetime import date
cmaior = 0
cmenor = 0

for i in range(1, 8):
    idades = int(input('\nDigite o ano de nascimento da {}° pessoa: '.format(i)))
    if date.today().year-idades >= 21:
       cmaior += 1
    else:
       cmenor += 1

print('\nNo total {} pessoas são maiores de idade e {} não atingiram a maioridade ainda'.format(cmaior, cmenor))