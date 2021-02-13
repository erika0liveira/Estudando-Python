nome = str(input('Digite o nome do(a) funcionário(a): '))
sal = float(input('Digite o salário do funcionário(a) {}: '.format(nome)))

if sal > 1250:
    print('\nO salário informado terá aumento de 10%. Totalizando R$ {:.2f}'.format(sal + ((sal * 10) / 100)))
else:
    print('\nO salário informado terá aumento de 15%. Totalizando R$ {:.2f}'.format(sal + ((sal * 15) / 100)))
