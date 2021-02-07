# Real para Dólar

real = float(input('Digite o valor em reais: R$ '))

dolar = 5.37  # 07/02/21

print('\nCom R$ {:.2f}, você pode comprar aproximadamente $ {:.2f}'.format(real, (real / dolar)))
