produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00,
            'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Caneta', 22.30, 'Livro', 34.90)

print('-'*50)
print(f'{"LISTAGEM DE PREÇOS":^50}')
print('-'*50)

for i in range(len(produtos)):
    if i % 2 == 0:
        print(f'{produtos[i]:.<40}', end='R$')
        print(f'{produtos[i+1]:>8.2f}\n', end='')
print('-'*50)
