v = int(input('Qual a velocidade do carro?: '))

if v > 80:
    print('\nLimite ultrapassado!\nCarro multado em R$ {:.2f}'.format(7*(v-80)))
else:
    print('\nNão ultrapasse o limite de 80KM')