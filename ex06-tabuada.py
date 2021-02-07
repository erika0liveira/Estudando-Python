num=int(input('Digite um número: '))
max=int(input('Quer multiplica-lo por quantas vezes? '))

print('\n')

for i in range (max+1):
    print('{} X {} = {}'.format(num, i, (num*i)))
    i+=1