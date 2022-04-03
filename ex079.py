lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    print('Valor adicionado com sucesso...')
    cont = str(input('Deseja continuar? (S/N) ').upper())
    if cont == 'N':
        break
lista.sort()
print(f'Você digitou os números: {lista}')