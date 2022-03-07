from random import randint
from time import sleep

num_maq = randint(0, 10)
cont = 0

print('_=_'*10)
print('Pense em um número de 0 a 10...')
print('_=_'*10)
num_pessoa = int(input('Qual número você pensou? '))
print('PROCESSANDO...\n')
sleep (1)

if num_pessoa == num_maq:
    print('ACERTÔ MISERÁVI!!!')
    print('Você acertou na {}ª vez'.format(cont))
else:
    print('ERRROOOU!!!')
    cont += 1

while num_pessoa != num_maq:
    num_pessoa = int(input('Tente outra vez: '))
    print('PROCESSANDO...\n')
    sleep(1)

    if num_pessoa == num_maq:
        print('ACERTÔ MISERÁVI!!!')
        print('Você acertou na {}ª vez'.format(cont))
    else:
        print('ERRROOOU!!!')
        cont +=1