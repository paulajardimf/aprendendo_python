largura = float(input('Insira a largura da parede: '))
altura = float(input('Insira a altura da parede: '))
metragem_quadrada = largura*altura
print('Sua parede tem a dimensão de {:.2f} x {:.2f}, totalizando {:.2f} m²'.format(largura, altura, metragem_quadrada))
print('Você precisará utilizar {} litros de tinta para pintar esta parede'.format(metragem_quadrada//2))

