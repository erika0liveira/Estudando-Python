from random import randint
from time import sleep

print('\n\033[1;36m********* ADVINHE O NÚMERO **********\033[m')

num = int(input('\n\033[1;36mEscolha um número entre 0 e 10: \033[m'))
numPC = randint(0, 10)

print('\n\033[1;36mProcessando...\033[m')
sleep(1)

if num == numPC:
    print('\n\033[1;32mVocê acertou, parabéns!\033[m')
else:
    print('\n\033[1;31mQue pena, não foi dessa vez!\033[m')

print('\n\033[1;36mO número escolhido pelo computador foi:\033[m \033[1;36m{}\033[m.'.format(numPC))