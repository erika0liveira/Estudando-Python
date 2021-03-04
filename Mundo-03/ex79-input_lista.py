numeros = [int(input('Digite um número: '))]
while True:
    n = input('\nQuer adicionar mais um número?\nSim = número / Não = qualquer letra: ')
    while n.isdigit() is True and int(n) in numeros:
        n = input('\nHmm... Esse número já foi adicionado, tente outro: ')
    if n.isdigit() is False:
        print(f'\n{"* " * 15}\n{"ENCERRADO":^30}\n{"* " * 15}')
        break
    if int(n) not in numeros:
        numeros.append(int(n))
print(f'\nOs números digitados em ordem crescente são: {sorted(numeros)}')
