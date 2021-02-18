s = 0
c = 0

for i in range(1, 501, 2):
    if i % 3 == 0:
        s += i
        c += 1

print('A soma dos {} números ímpares e divisíveis por 3, entre 1 e 500 é: {}'.format(c, s))
