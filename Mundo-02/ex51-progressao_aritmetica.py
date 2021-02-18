#Primeiro termo
pt = int(input('Digite o PRIMEIRO TERMO da progressão aritmética: '))

#Razão
r = int(input('\nDigite a RAZÃO da progressão aritmética: '))

print('\nPA: ', end= '')

for i in range (pt, pt + (r * 10), r):
    if i >= (pt + (r * 9)):
        print(i, end= ' \n')
    else:
        print(i, end=' -> ')
