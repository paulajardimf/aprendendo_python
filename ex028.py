from random import randint
from time import sleep

num_maq = randint(0, 5)
print('_=_'*10)
print('Pense em um número de 1 a 5...')
print('_=_'*10)
num_pessoa = int(input('Qual número você pensou? '))
print('PROCESSANDO...')
sleep (2)

if num_pessoa == num_maq:
    print('ACERTÔ MISERÁVI!!!')
else:
    print('ERRROOOU!!! O número que eu pensei é {}'.format(num_maq))
