import random

print('\n********* ADVINHE O NÚMERO **********')

num = int(input('\nEscolha um número entre 0 e 10: '))
numPC = random.randint(0, 10)

print('\nO número escolhido pelo computador foi: {}.'.format(numPC))

if num == numPC:
    print('\nVocê acertou, parabéns!')
else:
    print('\nQue pena, não foi dessa vez!')
