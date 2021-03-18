# Resolução dos exercícios 107, 108, 109 e 110

from uteis import moeda, design

p = float(input('Digite um valor em R$ '))
design.seplin()
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'A metade de R$ {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O valor de R$ {moeda.moeda(p)} com 13% de redução é {moeda.diminuir(p, 13, True)}')
print(f'O valor de R$ {moeda.moeda(p)} com 10% de aumento é {moeda.aumentar(p, 10, True)}')
