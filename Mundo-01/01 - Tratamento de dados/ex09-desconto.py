# Calcular 5% de desconto no valor de um produto

produto = str(input('Digite o nome do produto: '))
preco = float(input('Digite o preço do produto: '))

print('\nProduto: {}\nPreço: R$ {:.2f}\nDesconto de 5%: R${:.2f}\nPreço final: R$ {:.2f}'.format(produto, preco, (preco*0.05), (preco-(preco*0.05))))