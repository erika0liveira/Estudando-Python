aluno = {}
resultado = []
situacao = ''
c = ''

while True:
    aluno['Nome'] = str(input('\nDigite o nome do aluno: '))
    aluno['Media'] = float(input('Digite a média do aluno: '))

    if aluno['Media'] >= 7:
        aluno['Situacao'] = 'Aprovado'
    elif 5.5 <= aluno['Media'] <= 6:
        aluno['Situacao'] = 'Em recuperação'
    else:
        aluno['Situacao'] = 'Reprovado'
    resultado.append(aluno.copy())

    print()
    print('-' * 62)
    for k in aluno:
        if k == 'Situacao':
            print(f'{k:^20}'.upper())
        else:
            print(f'{k:^20}'.upper(), end='|')
    print('-' * 62)

    for v in aluno.values():
        if v == 'Aprovado' or v == 'Reprovado' or v == 'Em recuperação':
            print(f'{v:^20}'.upper())
            print('-' * 62)
        else:
            print(f'{v:^20}'.upper(), end='|')

    c = str(input('\nQuer ver a situação de mais um aluno? [S/N]: ')).upper()[0]

    if c != 'S':
        print('Ok, programa encerrado.')
        break
