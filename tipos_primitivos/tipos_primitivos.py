var = input('Digite algo: ')

print('Você digitou: {}'.format(var))
print(type(var))
print('Esta em maiusculo: {}'.format(var.isupper()))
print('É alfanúmerico?: {}'.format(var.isalnum()))
print('Da para ser impresso?: {}'.format(var.isprintable()))
