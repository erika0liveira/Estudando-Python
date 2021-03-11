import datetime

info = {}

while True:
    info['Nome'] = str(input('Digite o nome: '))
    ano = int(input('Digite o ano de nascimento: '))
    info['Idade'] = datetime.date.today().year - ano
    info['CTPS'] = int(input('Número do CTPS [0 não tem]: '))

    if info['CTPS'] == 0:
        break
    else:
        info['Contratacao'] = int(input('Ano de contratação: '))
        info['Aposentadoria'] = (35 - (datetime.date.today().year - info['Contratacao'])) + info['Idade']
        info['Salario'] = float(input('Salario: R$ '))
        break

print()
for v in info:
    print(f'{v} é {info[v]}')
