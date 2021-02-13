nome = str(input('Digite o nome do(a) funcionário(a): '))
sal = float(input('Digite o salário do funcionário(a) {}: '.format(nome)))

if sal > 1250:
    print('\nO salário de \033[1m{}\033[m em \033[1;31mR$ {}\033[m terá aumento de \033[1;32m10%\033[m. Totalizando \033[1;32mR$ {:.2f}\033[m'.format(nome, sal, sal + ((sal * 10) / 100)))
else:
    print('\nO salário de \033[1m{}\033[m em \033[1;31mR$ {}\033[m terá aumento de \033[1;32m15%\033[m. Totalizando \033[1;32mR$ {:.2f}\033[m'.format(nome, sal, sal + ((sal * 15) / 100)))
