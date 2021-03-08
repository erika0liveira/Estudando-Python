alunos = []
aux = []
media = []
continua = ''
detalhe = ''
linha = 0

print(f'{"-" * 60}')
print(f'{" MÉDIA DOS ALUNOS ":^60}')

while True:
    print('-' * 60)
    aux.append(str(input('Digite o nome do aluno: ')))
    for i in range(2):
        aux.append(float(input(f'Digite a {i+1}ª nota: ')))
    print('-' * 60)
    alunos.append(aux[:])
    if len(aux) > 2:
        aux.clear()

    continua = str(input('Quer continuar? [S/N]: ')).upper()[0]
    if continua != 'S':
        break

for n in alunos:
    if n[1] not in media:
        media.append(sum(n[1:3])/2)

print('\n')
print(f'{"-" * 60}')
print(f'{" RESULTADOS ":^60}')
print(f'{"-" * 60}')
print(f'{"N°":^20}{"|"}{"NOME":^20}{"|"}{"MÉDIA":^20}')
while linha < len(alunos):
    print(f'{"-" * 60}')
    print(f'{linha+1:^20}', end='|')
    print(f'{alunos[linha][0]:^20}', end='|')
    print(f'{media[linha]:^20.1f}')
    linha += 1
print(f'{"-" * 60}')

while True:
    detalhe = input('\nQuer ver as notas de algum aluno? [Sim = N° / Não = Qualquer Letra: ')
    if not detalhe.isdigit() or int(detalhe) > len(alunos):
        print('\nOk. Programa Encerrado!')
        break
    else:
        print(f'\nAs notas de {alunos[int(detalhe)-1][0]} são: {alunos[int(detalhe)-1][1:3]}')
