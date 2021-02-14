import math

#Mostrar apenas a porção inteira de um número real

num = float(input('Digite um número real: '))
print('A porção inteira deste número é: {}\n'.format(math.floor(num)))

print('#'*100)

#Calcular a hipotenusa

op = float(input('Qual o tamanho do cateto oposto? '))
ad = float(input('Qual o tamanho do cateto adjacente? '))

print('O comprimento da hipotenusa é: {:.2f}\n'.format(math.hypot(op, ad)))

#Calcular Seno, Cosseno e Tangente de um angulo

ang = float(input('Digite o angulo: '))

s = math.sin(math.radians(ang))
c = math.cos(math.radians(ang))
t = math.tan(math.radians(ang))

print('Seno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(s, c, t))