print('''\n****** CONVERSOR DE INT ******

1 - Converter para \033[1;33mBinário\033[m
2 - Converter para \033[1;35mOctal\033[m
3 - Converter para \033[1;36mHexadecimal\033[m
0 - Sair do programa''')

while True:
    try:
        x = int(input('\nSelecione o tipo de operação: '))
    except ValueError:
        print('\nPor favor, digite uma opção válida.')
        continue
    if x > 4:
        print('\nEscolha um número válido!')
        continue
    else:
        break

if x == 0:
    print('\n\033[1;31mPrograma encerrado!\033[m')
else:
    num = int(input('\nDigite o número inteiro a ser convertido: '))

if x == 1:
    print('\nO número {} em \033[1;33mBinário\033[m fica {}'.format(num, bin(num)[2:]))
elif x == 2:
    print('\nO número {} em \033[1;35mOctal\033[m fica {}'.format(num, oct(num)[2:]))
elif x == 3:
    print('\nO número {} em \033[1;36mHexadecimal\033[m fica {}'.format(num, hex(num)[2:]))


