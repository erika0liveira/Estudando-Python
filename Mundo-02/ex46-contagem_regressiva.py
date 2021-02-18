from time import sleep
import emoji

print('\n{:*^29}\n'.format(' CONTAGEM REGRESSIVA '))

for i in range (10, -1, -1):
    sleep(1)
    print('{} {:02d} {}'.format('. '*6, i, ' .'*6))
sleep(1)

print('\n{:^20}\n'.format((emoji.emojize(':fireworks:') * 3) + ' FELIZ ANO NOVO! ' + (emoji.emojize(':fireworks:') * 3)))





