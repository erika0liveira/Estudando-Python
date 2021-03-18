from uteis import moeda, dado

v = dado.validaMoeda(input('Digite um valor em R$ '))
aum = float(input('Digite a % de aumento: R$ '))
dim = float(input('Digite a % de redução: R$ '))
moeda.resumo(v, aum, dim)
