# "Caderno" de anotações do Curso em Vídeo sobre Python - Mundo 1

# Variáveis basicas
nome = 'Erika'
idade = 21
peso = 60.0

# Concatenando com ',' (diversos tipos de var)
print(nome, idade, peso)

# Concatenando com '+' (mesmo tipo de variável)
print(nome + ' ' + str(idade) + ' ' + str(peso))

# Quebra de linha
print('--------------------------------------------------------')

# Desafio 01 - Receber nome e dar as boas vindas
nomeUsuario = input('Qual o seu nome?\n')
#idadeUsuario = input('Agora digite a sua idade\n')
#pesoUsuario = input('Por último, diga seu peso\n')

print('\nOlá ' + nomeUsuario + ' seja benvindo(a)!')

# Desafio 02 - Data de nascimento
dia = int(input('\nDigite em 02 digitos o dia em que você nasceu\n'))
if(len(str((dia)))) < 1 or len(str((dia))) > 2:
        print('Por favor, digite apenas dois números')
else:
    mes = int(input('\nAgora digite o mês\n'))
    if(len(str((mes)))) < 1 or len(str((mes))) > 2:
        print('Por favor, digite apenas dois números')
    else:
        ano = int(input('\nPor fim, digite o ano do seu nascimento\n'))
        if(len(str((ano)))) < 2 or len(str((ano))) == 3 or len(str((ano))) > 4:
            print('Por favor, digite apenas dois números')
        else:
            print('\n', nomeUsuario+',', ' você nasceu em: ', dia, '/', mes, '/', ano, '!\n')

# Desafio 03 - Soma
num1 = int(input('\nDigite o primeiro número: '))
num2 = int(input('\nDigite o segundo número: '))

print('\nO resultado da soma é: ', num1 + num2)



