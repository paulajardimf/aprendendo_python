largura = float(input('Insira a largura da parede: '))
altura = float(input('Insira a altura da parede: '))
metragem_quadrada = float(largura*altura)
print('Você precisará utilizar {} litros de tinta para pintar esta parede'.format(metragem_quadrada//2))

