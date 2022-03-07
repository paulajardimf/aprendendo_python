#progressão aritmética

primeiro = int(input('Insira o primeiro termo: '))
r = int(input('Insira a razão: '))
termo = primeiro
cont = 1

while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += r
    cont += 1
print('FIM')