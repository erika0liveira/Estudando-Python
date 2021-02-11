# Calcular a área de uma parede e a quantidade de tinta necessária para pinta-la, sendo que cada litro pinta 2m²

larg = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))

print('\nA parede tem a seguinte dimensão: {} X {}, dessa forma a área total é: {:.2f} mt².\nSera necessário, aproximadamente, {:.1f} litro(s) de tinta'.format(larg, altura, (larg*altura), ((larg*altura)/2)))

