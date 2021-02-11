import math

#Mostrar apenas a porção inteira de um número real

num = float(input('Digite um número real: '))
print('A porção inteira deste número é: {}\n'.format(math.floor(num)))

print('#'*100)

#Calcular a hipotenusa

op = float(input('Qual o tamanho do cateto oposto? '))
ad = float(input('Qual o tamanho do cateto adjacente? '))

print('O comprimento da hipotenusa é: {}\n'.format(math.hypot(op, ad)))

#Calcular Seno, Cosseno e Tangente de um angulo

ang = float(input('Digite o angulo: '))

print('Seno: {}\nCosseno: {}\nTangente: {}'.format(math.sin(ang), math.cos(ang), math.tan(ang)))