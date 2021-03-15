def leiaint(n) -> object:
    while True:
        if not n.isdigit():
            n = input('\033[1;31m\nERRO!\033[m\nDigite apenas um número inteiro: ')
        elif n.isdigit():
            return f'\nVocê digitou {n}'


num = leiaint(input('Digite um número: '))
print(num)
