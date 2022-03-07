num = cont = soma = 0
num = int(input('Insira um número, ou digite 999 para encerrar: '))

while num != 999:
    cont += 1
    soma += num
    num = int(input('Insira um número, ou digite 999 para encerrar: '))

print('Você digitou {} números'.format(cont))
print('A soma entre eles é {}'.format(soma))
