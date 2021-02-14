v = float(input('Qual a velocidade do carro?: '))

if v > 80:
    print('\nLimite ultrapassado!\nCarro multado em \033[1;31mR$ {:.2f}\033[m'.format(7*(v-80)))

print('\nNão ultrapasse o limite de 80KM/h. Dirija sempre com segurança')