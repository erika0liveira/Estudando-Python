num = int(input('Digite um número de 0 a 9999:'))

print('Unidade: {}\nCentena: {}\nDezena: {}\nMilhar: {}'.format((num // 1 % 10), (num // 10 % 10), (num // 100 % 10), (num // 1000 % 10)))


