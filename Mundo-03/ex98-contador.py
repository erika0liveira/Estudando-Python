from time import sleep

def contador(a, b, c):
    if c == 0:
        c = 1
    elif c < 0:
        c *= -1
    print(f'Contagem de {a} até {b} de {abs(c)} em {abs(c)}:')
    if a < b:
        for i in range(a, b+1, c):
            print(i, end=' ', flush=True)
            '''sleep(0.5)'''
    elif a > b:
        for i in range(a, b-1, -c):
            print(i, end=' ', flush=True)
            '''sleep(0.5)'''
        if c < 0:
            c *= -1
            for i in range(a, b-1, c):
                print(i, end=' ', flush=True)
                '''sleep(0.5)'''
    print('FIM!')
    print('-' * 50)


print('-' * 50)
contador(1, 10, 1)
contador(10, 0, 2)
contador(a=int(input('INÍCIO: ')),
         b=int(input('FIM: ')),
         c=int(input('INÍCIO: ')))
