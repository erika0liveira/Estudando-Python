from datetime import date

nome = str(input('Qual o nome do atléta? '))
nas = int(input('Qual o ano de nascimento? '))

categoria = 'none'

if date.today().year - nas <= 9:
    categoria = 'Mirim'
elif date.today().year - nas <= 14:
    categoria = 'Infantil'
elif date.today().year - nas <= 19:
    categoria = 'Júnior'
elif date.today().year - nas <= 25:
    categoria = 'Sênior'
else:
    categoria = 'Master'

print('\n{} tem {} ano(s) de idade e pertence a categoria {}'.format(nome, date.today().year - nas, categoria))