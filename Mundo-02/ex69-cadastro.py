continuar = ''
i = ''
s = 'x'
maior = 0
m = 0
f = 0

while True:

    print('\n')
    print('~ '*26)
    print('{:^50}'.format('CADASTRO DE PESSOAS'))
    print('~ '*26)
    print('\n')
    print('-' * 50)

    while not isinstance(i, int):
        i = int(input('Digite a idade: '))
        if isinstance(i, int):
            if i >= 18:
                maior += 1

    while 'F' != s != 'M':
        s = str(input('Digite a sexo MASCULINO ou FEMININO [M/F]: ')).upper().strip()[0]
        if s == 'M':
            m += 1
        if s == 'F' and i < 20:
            f += 1

    while 'N' != continuar != 'S':
        continuar = str(input('Deseja cadastrar mais uma pessoa? [S/N]: ')).upper().strip()[0]
        i = 'x'
        s = 'x'

    print('-' * 50)

    if continuar == 'N':
        break
    elif continuar == 'S':
        continuar = ''

print('~ '*26)
print('{:^50}'.format('FIM DO CADASTRO'))
print('~ '*26)

if maior == 0:
    print('\nNenhuma pessoa tem mais de 18 anos')
elif maior == 1:
    print(f'\n{maior} pessoa tem mais de 18 anos')
elif maior > 1:
    print(f'\n{maior} pessoas tem mais de 18 anos')

if m == 0:
    print('Nenhum homem foi cadastrado')
elif m == 1:
    print(f'{m} homem foi cadastrado')
elif m > 1:
    print(f'{m} homens foram cadastrados')

if f == 0:
    print('Nenhuma mulher com menos de 20 anos foi cadastrada')
elif f == 1:
    print(f'{f} mulher com menos de 20 anos foi cadastrada')
elif f > 1:
    print(f'{f} mulheres com idade de 20 anos ou menos foram cadastradas')
