c = ''
produtos = []
valores = []
nome = ''
preco = 0
maior = 0

print('~ '*26)
print('{:^50}'.format('CARRINHO DE COMPRAS'))
print('~ '*26)

while True:
    print('\n')

    print('-' * 50)
    nome = str(input('Digite o nome do produto: ')).strip()
    produtos.append(nome)

    preco = float(input('Digite o valor R$ '))
    valores.append(preco)

    while 'N' != c != 'S':
        c = str(input('Deseja cadastrar mais um produto? [S/N]: ')).upper().strip()[0]
    if c == 'N':
        break
    elif c == 'S':
        c = ''
    print('-' * 50)

print('~ '*26)
print('{:^50}'.format('FIM DO PROGRAMA'))
print('~ '*26)

print(f'\nO total das compras deu R$ {sum(valores):.2f}')

for i in range(len(valores)):
    if valores[i] > 1000:
        maior += 1

if maior == 0:
    print('Nenhum produto custou mais R$ 1.000,00')
elif maior == 1:
    print('1 produto custou mais de R$ 1.000,00')
else:
    print(f'{maior} produtos custaram mais de R$ 1.000,00')

menor = valores.index(min(valores))

print(f'O item mais barato foi {produtos[menor]} e custou R$ {min(valores):.2f}')
