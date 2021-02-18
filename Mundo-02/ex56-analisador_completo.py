soma = 0
c = 0
idadeH = 0
nomeH = ''

for i in range(1, 5):
    print('\n{} {}° PESSOA {}'.format('-'*20, i, '-'*20))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    gen = str(input('Homem[H] ou Mulher[M]: ')).upper().strip()
    print('-'*51)
    soma += idade

    if gen == 'HOMEM' or gen == 'H':
        if idadeH < idade:
            idadeH = idade
            nomeH = nome

    if gen == 'MULHER' or gen == 'M':
        if idade < 20:
            c += 1

print('\n{} RESULTADOS {}'.format('-'*25, '-'*25))
print('A média das idades informadas é de {:.0f} anos'.format(soma/4))

if idadeH > 0:
    print('O homem mais velho tem {} anos de idade e se chama "{}"'.format(idadeH, nomeH))

if c == 1:
    print('{} mulher possui menos de 21 anos'.format(c))
if c > 1:
    print('{} mulheres possuem menos de 21 anos'.format(c))
