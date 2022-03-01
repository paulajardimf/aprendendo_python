velocidade = int(input('Qual a velocidade do carro? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Você foi multado em R$ {}.'.format(multa))
else:
    print('Você está dentro do limite legal.')