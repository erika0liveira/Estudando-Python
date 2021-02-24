while True:
    num = int(input('Digite um número para ser multiplicado: '))

    if num < 0:
        print('\n\033[1;31mPrograma encerrado!\033[m')
        break

    else:
        max = int(input('Quer multiplica-lo por quantas vezes? '))
        print('-' * 20)
        for i in range(max+1):
            print('{} X {:02d} = {:02d}'.format(num, i, (num*i)))
            i += 1
        print('-' * 20)
