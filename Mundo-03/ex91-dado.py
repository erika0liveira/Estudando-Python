from random import randint
from time import sleep

c = 1
dice = {}
sorteio = []

print()
print(f'{" SORTEIO DOS DADOS ":-^32}')
print()
for i in range(1, 7):
    dice['Jogador'] = i
    dice['Dado'] = randint(1, 6)
    sleep(1)
    print(dice)
    sorteio.append(dice.copy())
    dice.clear()
    c += 1

sleep(1)
print()
print(f'{"RANKING DOS GANHADORES":^31}')
print('\nProcessando', end='')
sleep(0.5)
print('.', end='')
sleep(0.5)
print('.', end='')
sleep(0.5)
print('.\n')

organizado = sorted(sorteio, key=lambda k: k['Dado'], reverse=True)
for v in organizado:
    print(f'{v["Jogador"]}° Jogador -', end=' ')
    print(f'Sorteio do dado: {v["Dado"]}')
