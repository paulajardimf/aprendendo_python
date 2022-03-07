num = 0
continuar = 's'
media = soma = cont = maior = menor = 0

while continuar in 'sS':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    continuar = str(input('CONTINUAR? [S/N]: ')).upper().strip()[0]

media = soma / cont
print('A média entre os valores inseridos é {:.2f}'.format(media))
print('O maior valor foi {}, e o menor valor foi {}'.format(maior, menor))

