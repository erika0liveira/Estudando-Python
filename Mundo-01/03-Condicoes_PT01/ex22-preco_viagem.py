distancia = float(input('Informe a distância em KM da viagem: '))

#Maneira "convencional"
if distancia <= 200:
    print('\nO preço desta viagem de {} KM será de R$ {:.2f}'.format(distancia, distancia * 0.50))
else:
    print('\nO preço desta viagem de {} KM será de R$ {:.2f}'.format(distancia, distancia * 0.45))

'''#Maneira simplificada
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('\nO preço desta viagem de {} KM será de R$ {:.2f}'.format(distancia, preco))'''


