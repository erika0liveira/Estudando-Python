# Faça um programa que leia o antecessor, sucessor, dobro, triplo, raiz quadrada e cúbica de um número
num = int(input('Digite um número: '))

print('Seu numero é:{}'.format(num))
print('Antecessor: {}\nSucessor: {}'.format(num-1, num+1))
print('Raiz Quadrada: {}\nRaiz Cúbica: {}\n'.format(num**(1/2), num**(1/3)))

print('*'*50)


