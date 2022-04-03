lista =[]
for cont in range(0,5):
    lista.append(int(input(f'Digite um valor para a posição {cont}: ')))
print(f'Você digitou os números {lista}')
print(f'O maior valor digitado foi: {max(lista)} na posição {lista.index(max(lista))}')
print(f'O menor valor digitado foi: {min(lista)} na posição {lista.index(min(lista))}')
