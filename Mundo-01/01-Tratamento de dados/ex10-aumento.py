# Aumento salarial de 15%

nome = str(input('Digite o nome do(a) funcionário(a): '))
sal = float(input('Digite o salário do funcionário(a) {}: '.format(nome)))

print('\nFuncionário(a): {}\nSalário atual: R$ {:.2f}\nReajuste de 15%: R$ {:.2f}\nNovo Salário: R${:.2f}'. format(nome, sal, (sal*0.15), (sal+(sal*0.15))))