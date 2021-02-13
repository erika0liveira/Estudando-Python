distancia = float(input('Informe a distância em KM da viagem: '))

if distancia <= 200:
    print('\nO preço desta viagem de {} KM será de R$ {:.2f}'.format(distancia, distancia*0.50))
else:
    print('\nO preço desta viagem de {} KM  será de R$ {:.2f}'.format(distancia, distancia * 0.45))