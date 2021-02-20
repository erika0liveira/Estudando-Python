continua = 'S'
c = []

while continua == 'S':
    n = int(input('\nDigite um número: '))
    c.append(n)
    continua = str(input('Quer Ler mais um número? [S/N]: ')).upper()
    if continua != 'S':
        print('\n{:-^100}'.format(' RESULTADOS '))
        print('\nVocê digitou {} números {}'.format(len(c), c))
        print('Soma: {}'.format(sum(c)))
        print('Média {:.1f}'.format((sum(c)) / len(c)))
        print('Maior número: {}\nMenor número: {}'.format(max(c), min(c)))

