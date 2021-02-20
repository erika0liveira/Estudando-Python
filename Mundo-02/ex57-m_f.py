gen = str(input('Digite seu sexo [M/F]: ')).upper().strip()[0]

while gen not in 'MF':
    gen = str(input('Por favor, digite apenas Masculino [M] ou Feminino [F]: ')).upper()

print('\nSexo {} registrado!'.format(gen))
