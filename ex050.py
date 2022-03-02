soma = int(0)
for c in range (0,6):
    num = int(input('Digite um número qualquer: '))
    if num % 2 == 0:
        soma = soma + num

print('A soma entre os números pares é {}'.format(soma))