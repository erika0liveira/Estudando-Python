num=int(input('Digite um número para ser multiplicado: '))
max=int(input('Quer multiplica-lo por quantas vezes? '))

print('\n')

for i in range (max+1):
    print('{} X {:02d} = {:02d}'.format(num, i, (num*i)))
    i+=1