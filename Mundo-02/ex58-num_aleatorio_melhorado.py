# Desafio para melhorar o exercicio 19 do mundo 01 parte 03-Condições

from random import randint
from time import sleep

tot = 0
num = 100
numPC = 0
sn = ''
c = 0
acertou = False

print('\n\033[1;36m{} ADVINHE O NÚMERO {}\033[m'.format('-' * 10, '-' * 10))

while not acertou or sn == 'S':

    print('\n\033[1;35mO computador está pensando em um número', end='')
    sleep(0.5)
    print('.', end='')
    sleep(0.5)
    print('.', end='')
    sleep(0.5)
    print('.\033[m')
    sleep(0.5)

    numPC = randint(0, 10)
    print('Pronto!')

    while num != numPC:

        num = int(input('\nSua vez! Escolha um número entre 0 e 10: '))

        if num == numPC:
            print('\n\033[1;32mO número escolhido pelo computador foi: {}\033[m'.format(numPC))
            print('\033[1;32mParabéns! Você acertou na {}ª tentativa\033[m'.format(tot+1))
            sn = str(input('\nGostaria de jogar novamente? Sim [S] ou Não [N]: ')).upper().strip()[0]
            acertou = True
            if sn == 'N':
                print('\n\033[1;35mObrigada por jogar!\033[m')
        else:
            if numPC > num:
                print('\n\033[1;31mMais... Tenta de novo!\033[m')
                tot += 1
            elif numPC < num:
                print('\n\033[1;31mMenos... Tenta de novo!\033[m')
                tot += 1
