print('\nOs números pares no intervalo de 1 a 50 são: ', end='')

'''for i in range(1, 51):
    if i % 2 == 0:
        if i != 50:
            print('{:02d}'.format(i), end=', ')
        else:
            print('{:02d}'.format(i), end='.')'''

#MÉTODO OTIMIZADO
for i in range(2, 51, 2):
    if i != 50:
        print('{:02d}'.format(i), end=', ')
    else:
        print('{:02d}'.format(i), end='.')