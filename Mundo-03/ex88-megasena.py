import random
from time import sleep

jogos = []
tam = 6

print('-'*40)
print(f'{"MEGA SENA":^40}')
print('-'*40)

qtd = int(input('Quantos jogos você quer gerar? '))

print(f'\nGerando os {qtd} jogos', end='')
sleep(0.3)
print('.', end='')
sleep(0.3)
print('.', end='')
sleep(0.3)
print('.\n')

while qtd > 0:
    jogos.append(random.sample(range(1, 60), 6))
    qtd -= 1

print('JOGOS GERADOS:')
for i in range(len(jogos)):
    print(f'{i+1}° JOGO: {sorted(jogos[i])}')
