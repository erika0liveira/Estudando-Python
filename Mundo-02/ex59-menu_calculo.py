num = {}
escolha = 0
continua = ''


def recebevalor():
    print('\n{}'.format('-' * 50))
    for i in range(1, 3):
        num[i] = float(input('Digite o {}° número: '.format(i)))
    print('-' * 50)


recebevalor()

while escolha != 5:
    print('''\n{:-^50}
    [1] - SOMAR
    [2] - MULTIPLICAR
    [3] - VERIFICAR O MAIOR
    [4] - DIGITAR NOVOS VALORES
    [5] - CANCELAR E SAIR\n{}'''.format('MENU', '-' * 50))

    escolha = int(input('\nEscolha uma opção do menu: '))

    if escolha == 1:
        print('\nA soma de {} e {} é: {}'.format(num[1], num[2], num[1] + num[2]))

    elif escolha == 2:
        print('\n{} multiplicado por {} é: {}'.format(num[1], num[2], num[1] * num[2]))

    elif escolha == 3:
        if num[1] > num[2]:
            print('\nO número {} é maior que {}'.format(num[1], num[2]))
        if num[1] < num[2]:
            print('\nO número {} é maior que {}'.format(num[2], num[1]))
        else:
            print('\nOs números {} e {} são iguais'.format(num[2], num[1]))

    elif escolha == 4:
        recebevalor()

    elif escolha != 4 and escolha != 5:
        continua = str(input('\nGostaria de fazer outra operação? [S/N]: ')).upper()
        if escolha != 'S':
            print('\nPrograma Encerrado!')
            break

print('\nPrograma Encerrado!')
