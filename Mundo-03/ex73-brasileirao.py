# Resultados de 2018

times = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', 'Atlético Mineiro', 'Atlético Paranaense',
         'Cruzeiro', 'Botafogo', 'Santos', 'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará',
         'Vasco da Gama', 'América Mineiro', 'Sport', 'Vitória', 'Paraná')

print('~ ~ ' * 30)
print('\nOs cinco primeiros classificados foram: ')
for i in range(0, 5):
    print(f'{i+1}° - {times[i]}')

print('~ ~ ' * 30)
print('\nOs quatro ultimos classificados foram: ')
for i in range(16, 20):
    print(f'{i+1}° - {times[i]}')

print('~ ~ ' * 30)
print('\nTimes em ordem alfabética: ')
for i in range(0, 20):
    print(sorted(times)[i])
print('~ ~ ' * 30)

print(f'\nA Chapecoense ficou em {times.index("Chapecoense")}° lugar')
print('~ ~ ' * 30)
