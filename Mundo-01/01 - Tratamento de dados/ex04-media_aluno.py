#Faça um programa que leia a média de um aluno

nome = str(input('Digite o nome do aluno: '))

notas = list(map(float, input('Digite as 5 notas do aluno separadas por espaço: ').split()))

for i in range (len(notas)):
    print('A {}° nota é: {}'.format(i+1, notas[i]))
    i+=1

print('A média deste aluno é: {}'.format((sum(notas))/5))
