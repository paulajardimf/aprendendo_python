print('{:=^40}'.format(' LOJAS ETCETERA '))
valor = float(input('Insira o valor do produto: R$ '))
print('''Formas de pagamento:
[ 1 ] A VISTA DINHEIRO/PIX 
[ 2 ] A VISTA CARTÃO 
[ 3 ] ATÉ 2X CARTÃO 
[ 4 ] 3X OU MAIS NO CARTÃO''')
condicao = int(input('Insira o código correspondente: '))

if condicao == 1:
    print('TOTAL A PAGAR: R$ {:.2f}'.format(valor - (valor * 0.10)))
elif condicao == 2:
    print ('TOTAL A PAGAR: R$ {:.2f}'.format(valor - (valor * 0.05)))
elif condicao == 3:
    print ('TOTAL A PAGAR R$ {:.2f}'.format(valor))
elif condicao == 4:
    print('TOTAL A PAGAR R$ {:.2f}'.format(valor+(valor * 0.20)))
else: print('CÓDIGO INVÁLIDO, TENTE NOVAMENTE')

