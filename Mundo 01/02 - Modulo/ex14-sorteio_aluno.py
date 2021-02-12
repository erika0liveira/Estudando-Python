from random import choice, shuffle

#Sortear aluno para limpar louse
nome = list(input('Digite os nomes para serem sorteados: ').split(', '))
print('\nO aluno escolhido para limpar a lousa foi: {}!\n'.format(choice(nome)))

#Sortear ordem de apresentação
print('A ordem para apresentação dos trabalhos será:')

shuffle(nome)

for i in range (len(nome)):
    print('{}° - {}'.format(i+1,nome[i]))