# Primeiro termo
primeiro = int(input('Digite o PRIMEIRO TERMO da progressão aritmética: '))

# Apenas para formatar o output
primeiroTermo = primeiro

# Iniciamos com 10 (exercício)
quantidade = 10

# Razão
r = int(input('\nDigite a RAZÃO da progressão aritmética: '))

# Ultimo termo
ultimo = primeiro + (r * quantidade)

while primeiro < ultimo:
    if primeiroTermo == primeiro:
        print('PA: {}'.format(primeiro), end='')
    else:
        print(' -> {} '.format(primeiro), end='')
    primeiro += r
    if primeiro == ultimo:
        quantidade = int(input('\n\nPara ver mais termos nesta razão digite o número, se não apenas digite 0: '))
        ultimo += r * quantidade
    if quantidade == 0:
        print('\nPrograma encerrado!')
        break

