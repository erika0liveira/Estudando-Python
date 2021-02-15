from datetime import date
import sys

genero = str(input('Você é homem ou mulher?: ')).upper()

if genero == 'MULHER' or genero == 'M':
    print('\nPara mulheres o alistamento militar não é obrigátorio e sim opcional.')
    sys.exit()
elif genero == 'HOMEM' or genero == 'H':
    print('\nPara homens o alistamento militar é obrigátorio.')
    nascimento = int(input('\nEm qual ano você nasceu?: '))
    idade = (date.today().year) - nascimento
    print('\nNeste ano de {} você completou/completará {} anos de idade.'.format(date.today().year, idade))
    if idade < 18:
        print('\nAinda não está na hora de se alistar!\nFaça o alistamento em {}'.format(
            (18 - idade) + date.today().year))
    elif idade == 18:
        print('\nCom 18 anos o alistamento deve ser feito entre 1º de janeiro a 30 de abril')
    else:
        print(
            '\nJá passou da hora de se alistar!\nVocê deveria ter se alistado em {} e está atrasado em {} ano(s)'.format(
                date.today().year - (idade - 18), idade - 18))
else:
    print('\nDigite um dos generos mencionados.')
    sys.exit()

