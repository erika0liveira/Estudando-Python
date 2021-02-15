#A partir deste arquivo a nomeação dos exercícios será de acordo com os exercícios do Curso em Vídeo

from time import sleep

print('\nSeja benvindo(a)!\nPara cálculo do empréstimo bancário, por favor responda o questionário.')

print('-'*50)
v = float(input('Qual o valor da casa? '))
print('-'*50)
s = float(input('Qual o seu salário mensal? '))
print('-'*50)
a = int(input('Em quantos anos deseja pagar o empréstimo? '))
print('-'*50)

print('\nCalculando...')
sleep(2)

#Calculo da prestação mensal da casa de acordo com os anos
pm = v / (a * 12)

#Calculo da porcentagem do salario
ps = (s * 30) / 100

if pm > ps:
    print('\nInfelizmente os critérios não foram atendidos... Empréstimo \033[1;31mNEGADO!\033[m\nAs parcelas mensais em {} anos seriam de: \033[1;33mR$ {:.2f}\033[m'.format(a, pm))
else:
    print('\nParabéns, empréstimo \033[1;32mAPROVADO!\033[m\nAs parcelas mensais em {} anos serão de: \033[1;33mR$ {:.2f}\033[m'.format(a, pm))