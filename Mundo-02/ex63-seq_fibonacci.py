n = int(input('\nDigite a quantidade de números que quer ver: '))

anterior = 0
intermediario = 1
atual = 1
contador = 3

print('Sequencia de Fibonacci em {} números: {} -> {} -> '.format(n, anterior, intermediario), end='')

while contador <= n:
    atual = anterior + intermediario
    print(atual, end=' -> ')
    anterior = intermediario
    intermediario = atual
    contador += 1
print('FIM')

