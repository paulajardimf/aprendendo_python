dias = int(input('Qual a quantidade de dias alugados? '))
km = float(input('Qual a quantidade de km rodados? '))
diaria_carro = 60.00
km_rodado = 0.15
print('Aluguel do carro: R$ {:.2f}'.format(dias*diaria_carro))
print('Combustível gasto: R$ {:.2f}'.format(km*km_rodado))
print('O total a pagar é R$ {:.2f}'.format(dias*diaria_carro+km*km_rodado))
