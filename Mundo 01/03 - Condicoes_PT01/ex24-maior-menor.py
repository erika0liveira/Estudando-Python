a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o segundo número: '))

#Analisando o menor valor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

#Analisando o maior valor
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('\nO menor valor é: {}\nO maior valor é: {}'.format(menor, maior))