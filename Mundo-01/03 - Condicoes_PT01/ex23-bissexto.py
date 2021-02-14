from datetime import date

ano = int(input('Informe o ano para saber se ele é bissexto. Digite 0 para o ano atual: '))

if ano == 0:
    ano = date.today().year

if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
    print('\nO ano {} é um ano bissexto'.format(ano))
else:
    print('\nO ano {} não é um ano bissexto'.format(ano))