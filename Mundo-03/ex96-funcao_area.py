def area(a, b):
    print(f'A área total de {a} e {b} é {a * b}m².')
    print('-' * 50)
    print('\n')


print(f'{" CÁLCULO DE ÁREA ":-^50}')
while True:
    area(a=float(input('LARGURA: ')), b=float(input('COMPRIMENTO: ')))
    c = input('Deseja fazer mais um cálculo? [S/N]: ').upper()[0]
    if c == 'S':
        a = b = 0
        print('\n')
        print('-' * 50)
    else:
        print('PROGRAMA ENCERRADO')
        break
