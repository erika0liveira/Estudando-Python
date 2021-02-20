n = 0
c = []

print('\n{:-^50}'.format(' SOMA DE VÁRIOS NÚMEROS '))

while n != 999:
    n = int(input('\nDigite números para somar ou 999 para encerrar o programa: '))
    if n != 999:
        c.append(n)
print('\nVocê digitou {} números {} que somados resultam em {}'.format(len(c), c, sum(c)))