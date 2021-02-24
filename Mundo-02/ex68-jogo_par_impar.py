from random import randint
from time import sleep

escolha = ''

print('~ '*26)
print('{:^50}'.format('PAR OU ÍMPAR'))
print('~ '*26)

vitoria = 0

while True:

    print('\n\033[1;36mComputador está escolhendo um número...\033[m')
    sleep(1)
    pc = randint(0, 10)
    print('Pronto\n')
    valor = int(input('Sua vez, digite um valor: '))

    soma = pc + valor

    while 'P' != escolha != 'I':
        escolha = str(input('\nVocê escolhe Par ou Ímpar? [P/I]: ')).strip().upper()[0]

    print(f'\nVocê escolheu {valor} e o Computador {pc}. A soma foi {soma} ', end='')

    if escolha == 'P':
        if soma % 2 == 0:
            print('ou seja, deu Par. Parabens!\n\nVamos jogar novamente...\n')
            vitoria += 1
        elif soma % 2 > 0:
            print('ou seja, deu Ímpar.\n')
            break
    elif escolha == 'I':
        if soma % 2 == 0:
            print('ou seja, deu Par.\n')
            break
        if soma % 2 > 0:
            print('ou seja, deu Ímpar. Parabens!\n\nVamos jogar novamente...')
            vitoria += 1

    escolha = ''

print('~ '*26)
print('{:^50}'.format(' GAME OVER '))
print('~ '*26)

if vitoria == 0:
    print('\nQue pena, você não ganhou nenhuma vez :(')
elif vitoria == 1:
    print(f'\nVocê ganhou {vitoria} vez, parabéns!')
else:
    print(f'\nVocê ganhou {vitoria} vezes, parabéns!')
