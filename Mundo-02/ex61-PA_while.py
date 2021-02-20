# Primeiro termo
pt = int(input('Digite o PRIMEIRO TERMO da progressão aritmética: '))
ptermo = pt

# Razão
r = int(input('\nDigite a RAZÃO da progressão aritmética: '))

# Ultimo termo
ut = pt + (r * 10)

print('\nUSANDO FOR')
for i in range(pt, ut, r):
    if ptermo == i:
        print('PA: {}'.format(i), end='')
    else:
        print(' -> {} '.format(i), end='')

print('\n\nUSANDO WHILE')
while pt < ut:
    if ptermo == pt:
        print('PA: {}'.format(pt), end='')
    else:
        print(' -> {} '.format(pt), end='')
    pt += r
