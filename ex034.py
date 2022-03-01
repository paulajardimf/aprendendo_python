salario = float(input('Digite o valor do salário para calcular o aumento: R$ '))
salario_novo = float(0)

if salario >= 1250.00:
    salario_novo = (salario * 0.10) + salario
else:
    salario_novo = (salario * 0.15) + salario

print('O novo salário com aumento fica: R$ {:.2f}'.format(salario_novo))
