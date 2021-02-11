d = int(input('O carro foi alugado por quantos dias: '))
km = float(input('Informe a quantidade de KM rodados: '))

print('O total a pagar por este aluguel é: R$ {:.2f}'. format((d * 60) + (km * 0.15)))