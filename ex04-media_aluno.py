#Faça um programa que leia a média de duas notas
#nome=str(input('Digite o nome do aluno: '))

#n1=float(input('Primeira nota: '))
#n2=float(input('Segunda nota: '))

#print('A média do(a) aluno(a) {} é: {}'.format(nome, ((n1+n2)/2)))

#Tentativa com Array, média do aluno contando 5 notas
notas = list(map(float, input('Digite as 5 notas do aluno separadas por espaço: ').split()))

for i in range (len(notas)):
    print('A {}° nota é: {}'.format(i+1, notas[i]))
    i+=1

print('A média deste aluno é: {}'.format((sum(notas))/5))
