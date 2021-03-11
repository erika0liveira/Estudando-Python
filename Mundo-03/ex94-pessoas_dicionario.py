from time import sleep
info = {}
cadastro = []
media = totm = 0
while True:
    info['nome'] = (str(input('\nNome: ')).capitalize())
    info['sexo'] = (str(input('Sexo [F/M]: ')).upper())
    while info['sexo'] not in 'FM' or info['sexo'].isdigit():
        info['sexo'] = (str(input('Por favor, apenas F ou M: ')).upper())
    n = input('Idade: ')
    while not n.isdigit():
        n = input('Por favor, digite a idade apenas em números: ')
    if n.isdigit():
        info['idade'] = int(n)
    media += info['idade']
    cadastro.append(info.copy())
    esc = str(input('\nQuer continuar? ')).upper()
    while esc not in 'SN' or esc.isdigit():
        esc = str(input('\nPor favor, apenas Sim ou Não: ')).upper()
    if esc == 'N':
        print('\nProcessando', end='')
        sleep(0.5)
        print('.', end='')
        sleep(0.5)
        print('.', end='')
        sleep(0.5)
        print('.\n')
        break
media /= len(cadastro)
print(f'{" RESULTADOS ":-^30}')
print(f'-> O grupo é formado por {len(cadastro)} pessoas')
print(f'-> A média de idade do grupo é {media:.2f} anos')
print(f'-> As mulheres cadastradas foram: ')
for p in cadastro:
    if p['sexo'] == 'F':
        totm += 1
        print(f' * {p["nome"]}')
if totm == 0:
    print(' * Nenhuma mulher cadastrada')
print(f'-> Lista das pessoas com idade acima da média de {media}: ')
for p in cadastro:
    if p['idade'] > media:
        for k, v in p.items():
            print(f'{k} = {v};', end=' ')
        print()
print('PROGRAMA FINALIZADO')
