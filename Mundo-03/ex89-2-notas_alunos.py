# Solução do Guanabara
ficha = list()
while True:
    nome = str(input('Digite o nome do aluno: '))
    nota1 = float(input('A primeira nota: '))
    nota2 = float(input('A segunda nota: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar [S/N]: '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"N°":<4}{"NOME:<10"}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:>10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar as notas de qual aluno? 999 interrompe: '))
    if opc == 999:
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
