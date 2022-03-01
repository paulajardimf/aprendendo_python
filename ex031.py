distancia = float(input('Insira a distância da viagem em km: '))

if distancia > 200:
    preco = 0.45 * distancia
else:
    preco = 0.50 * distancia

print('O valor da passagem é R$ {}'.format(preco))