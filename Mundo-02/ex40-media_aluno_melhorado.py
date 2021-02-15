#Exercício Mundo-01/01-Tratamento de Dados/EX-04 implementado com condições if/elif/else

nome = str(input('Digite o nome do aluno: '))
notas = list(map(float, input('Digite as notas do aluno separadas por espaço: ').split()))

print('\n')

for i in range (len(notas)):
    print('A {}° nota é: {}'.format(i+1, notas[i]))
    i+=1

media = sum (notas) / len(notas)

print('\nA média de {} é: {:.1f}'.format(nome, media))

if media < 5.0:
    print('\n{} foi \033[1;31mREPROVADO(A)\033[m, pois não atingiu a média mínima de 5.0'.format(nome))
elif 7 > media >= 5:
    print('\n{} está de \033[1;33mRECUPERAÇÃO\033[m, pois não atingiu média 7.0'.format(nome))
else:
    print('\n{} está \033[1;32mAPROVADO(A)\033[m. Parabéns!'.format(nome))
