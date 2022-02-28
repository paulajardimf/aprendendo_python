import math
angulo = float(input('Insira um ângulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O seno do ângulo {}º é {:.2f}'.format(angulo, seno))
print('O cosseno do ângulo {}° é {:.2f}'.format(angulo,cosseno))
print('A tangente do ângulo {}º é {:.2f}'.format(angulo, tangente))
