import random
alu_1 = str(input('Digite o nome do(a) primeiro(a) aluno(a): '))
alu_2 = str(input('Digite o nome do(a) segundo(a) aluno(a): '))
alu_3 = str(input('Digite o nome do(a) terceiro(a) aluno(a): '))
alu_4 = str(input('Digite o nome do(a) quarto(a) aluno(a): '))
lista = [alu_1, alu_2, alu_3, alu_4]
random.shuffle(lista)
print('A ordem de apresentação dos trabalhos é: {}'.format(lista))