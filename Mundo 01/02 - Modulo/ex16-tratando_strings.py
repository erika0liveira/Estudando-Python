#Exercicios aula 09
nome = str(input('Digite seu nome completo: ')).strip() #tirando os espaços

#Transformando em Maiusculo e Minusculo
print('\nMaiúsculo: {}'.format(nome.upper()))
print('Minuscúlo: {}'.format(nome.lower()))

#Contando caracteres sem espaço
esp = (nome.count(' '))
print('\nSeu nome "{}" contém {} caracteres'.format(nome, len(nome)-esp))

#Contando caracteres primeiro e último nome
nomeSplit = nome.split()
print('\nSeu primeiro nome é "{}" e contém {} caracteres'.format(nomeSplit[0], len(nomeSplit[0])))
print('Seu último nome é "{}" e contém {} caracteres'.format(nomeSplit[-1], len(nomeSplit[-1])))

#Verificando se existe o nome "Silva"
if 'SILVA' in nome.upper():
    print('\nUm dos nomes é Silva')

#Contem a letra "A"?
print('O nome "{}", contém {} letra(s) "A"'.format(nome, nome.upper().count('A')))

print('''\nPrimeira vez que a letra "A" aparece é na {}° posição
Última vez que a letra "A" aparece é na {}° posição'''.format(nome.upper().find('A'), nome.upper().rfind('A')))



