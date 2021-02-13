from random import randint
from time import sleep

print('\n********* ADVINHE O NÚMERO **********')

num = int(input('\nEscolha um número entre 0 e 10: '))
numPC = randint(0, 10)

print('Processando...')
sleep(1)

if num == numPC:
    print('\nVocê acertou, parabéns!')
else:
    print('\nQue pena, não foi dessa vez!')

print('O número escolhido pelo computador foi: {}.'.format(numPC))