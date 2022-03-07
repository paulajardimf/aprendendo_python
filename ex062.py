#continuação progressão aritmética

primeiro = int(input('Insira o primeiro termo: '))
r = int(input('Insira a razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
    total  = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM')