soma = 0
homem = {}

for i in range (0, 4):
    print('\n')
    nome = str(input('Qual o nome da {}° pessoa? '.format(i+1)))
    idade = int(input('Qual a idade da {}° pessoa? '.format(i+1)))
    soma += idade
    gen = str(input('A {}° pessoa é Homem ou Mulher? '.format(i+1))).upper()

    if gen == 'HOMEM':
        homem[i] = nome, idade

print('\nA média das 4 idades informadas é: {}'.format(soma/4))
print(homem)
print(max(idade))
