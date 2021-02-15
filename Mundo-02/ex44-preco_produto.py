from time import sleep

cor = {'limpa': '\033[m', 'red': '\033[1;31m'}

print('\n{:-^56}'.format(' LOJA X - CONDIÇÕES DE PAGAMENTO '))
print('''1 - À VISTA - DINHEIRO OU CHEQUE - 10% DE DESCONTO
2 - À VISTA - CARTÃO - 5% DE DESCONTO
3 - EM ATÉ 2 VEZES NO CARTÃO - SEM DESCONTO
4 - 3 VEZES OU MAIS NO CARTÃO - 20% DE JUROS
0 - CANCELAR''')
print('-' * 56)

while True:
    try:
        x = int(input('Selecione o tipo de operação: '))
    except ValueError:
        print('-' * 56)
        print('{}Digite apenas números conforme o menu.{}'.format(cor['red'], cor['limpa']))
        print('-' * 56)
        continue
    if x > 4:
        print('-' * 56)
        print('{}Escolha uma das opções do menu.{}'.format(cor['red'], cor['limpa']))
        print('-' * 56)
        continue
    else:
        break

if x == 0:
    print('{}Compra Encerrada!{}'.format(cor['red'], cor['limpa']))
else:
    preco = float(input('\nQual o valor total das compras? R$ '))

    print('\nProcessando...\n')
    sleep(1)

    if x == 1:
        desconto = (preco * 10) / 100
        print('-' * 56)
        print('À VISTA - DINHEIRO OU CHEQUE\nPreço: R$ {:.2f}\nDesconto de 10%: R$ {:.2f}\nPreço final: R$ {:.2f}'.format(preco, desconto, preco - desconto))
    elif x == 2:
        desconto = (preco * 5) / 100
        print('-' * 56)
        print('À VISTA NO CARTÃO\nPreço: R$ {:.2f}\nDesconto de 5%: R$ {:.2f}\nPreço final: R$ {:.2f}'.format(preco, desconto, preco - desconto))
    elif x == 3:
        parcela = preco / 2
        print('-' * 56)
        print('PARCELADO EM 2 VEZES - SEM DESCONTO\nPreço: R$ {:.2f}\n1° Parcela: {:.2f}\n2° Parcela: {:.2f}'.format(preco, parcela, parcela))
    elif x == 4:
        print('-' * 56)
        vezes = int(input('\nEm quantas vezes você quer parcelar está compra? '))

        print('\nDividindo em {} vezes com 20% de juros, as parcelas serão:\n'.format(vezes))
        parcela = (preco + ((preco * 20) / 100)) / vezes
        for i in range (vezes):
            print('{}° parcela: R$ {:.2f}'.format(i + 1, parcela))
            i += 1
        print('\nValor total: R$ {:.2f}'.format(parcela * vezes))

print('-'*56)
