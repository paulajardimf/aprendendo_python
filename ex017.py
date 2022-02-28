import math
y = float(input('Insira o comprimento do cateto oposto: '))
x = float(input('Insira o comprimento do cateto adjacente: '))
h = math.hypot(x,y)
print('O comprimento da hipotenusa é {:.2f}'.format(h))

