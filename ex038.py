n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))

if n1 > n2:
    maior = n1
    menor = n2
    print('O número {} é maior que o {}.'.format(maior, menor))
elif n2 > n1:
    maior = n2
    menor = n1
    print('O número {} é maior que o {}'.format(maior, menor))
else: print('NÃO EXISTE VALOR MAIOR, OS DOIS VALORES INSERIDOS SÃO IGUAIS.')