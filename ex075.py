num = (int(input('Digite um número: ')),
       int(input('Digite um outro número: ')),
       int(input('Digite um mais um número: ')),
       int(input('Digite o último número: ')))
print(f'Você digitou os números: {num}')
print(f'O número 9 foi digitado {num.count(9)} vezes')

if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}ª posição')
else:
    print('O número 3 não foi digitado em nenhuma posição')

print('Os números pares foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')


