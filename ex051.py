#progressão aritmética

termo = int(input('Insira o primeiro termo: '))
r = int(input('Insira a razão: '))
decimo = termo + (10-1) * r

for c in range(termo, decimo + r, r):
    print('{} '.format(c), end="-> ")
print('ACABOU')