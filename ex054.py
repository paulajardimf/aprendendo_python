from datetime import date
ano_atual = date.today().year
contador_adultos = int(0)
contador_menores = int(0)

for c in range (0,7):
    nascimento = int(input('Insira o ano de nascimento da {}a pessoa: '.format(c+1)))
    if ano_atual - nascimento >= 21:
        contador_adultos = contador_adultos +1
    else:
        contador_menores = contador_menores +1

print('ANALISANDO...')
print('{} pessoas atingiram a maioridade'.format(contador_adultos))
print('{} pessoas são menores de idade'.format(contador_menores))
