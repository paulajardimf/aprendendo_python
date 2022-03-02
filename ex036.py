print('SIMULADOR DE EMPRÉSTIMO DE IMÓVEIS')
print('_'*30)
valor = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o salário do comprador? R$ '))
anos = int(input('Em quantos anos será pago? '))

meses = anos * 12
parcela = valor / meses

if parcela > (0.30 * salario):
    print('-- EMPRÉSTIMO NEGADO --')
    print('A parcela total não pode ultrapassar R$ {:.2f}'.format(salario*0.30))
    print('Você simulou uma parcela de R$ {:.2f}'.format(parcela))
    print('Pagamento em {} meses'.format(meses))
elif parcela < (0.30 * salario):
    print('Parcela simulada: R$ {:.2f}'.format(parcela))
    print('Pagamento em {} meses'.format(meses))
