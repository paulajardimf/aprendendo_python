n = int(input('Digite um número para visualizar a sua tabuada: '))
print('-'*12)

for c in range (1,10+1):
    print('{} X {:2} = {}'.format(n, c, n*c))
print('-' *12)