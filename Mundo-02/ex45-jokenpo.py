from random import randint
from time import sleep
import sys

print('\n\033[1;36mTENTE GANHAR DO COMPUTADOR NO PEDRA, PAPEL E TESOURA\033[m')
print('-'*55)
print('''
# # # # # JOKENPÔ # # # # # 
#                         #
#      0 - PAPEL          #
#      1 - PEDRA          #
#      2 - TESOURA        #
#                         #
#      9 - SAIR           #
#                         #
# # # # # # # # # # # # # # 
''')
print('-'*55)

jokenpo = ('PAPEL', 'PEDRA', 'TESOURA')

print('\n\033[1;36mComputador está escolhendo...\033[m')
sleep(1)
xpc = randint(0, 2)
print('Pronto!')

while True:
    try:
        x = int(input('\nSua vez: '))
    except ValueError:
        print('\nDigite apenas um número de 0 a 3.')
        continue
    if 9 != x > 3:
        print('\nEscolha um número válido!')
        continue
    else:
        break

if x == 9:
    print('\nJogo encerrado!')
    sys.exit()
elif xpc == 0 and x == 1 or xpc == 1 and x == 2 or xpc == 2 and x == 0:
    print('\n\033[1;31mCOMPUTADOR GANHOU!\033[m\nVocê escolheu {} e o Computador {}'.format(jokenpo[x], jokenpo[xpc]))
elif xpc == x:
    print('\n\033[1;33mEMPATE!\033[m\nVocê escolheu {} e o Computador {}'.format(jokenpo[x], jokenpo[xpc]))
else:
    print('\n\033[1;32mVOCÊ GANHOU!\033[m\nVocê escolheu {} e o Computador {}'.format(jokenpo[x], jokenpo[xpc]))

