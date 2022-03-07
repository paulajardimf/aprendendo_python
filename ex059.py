total = 0
num1 = float(input('Insira o primeiro número: '))
num2 = float(input('Insira o segundo número: '))

print('''Operações disponíveis
[ 1 ] Somar;
[ 2 ] Multiplicar;
[ 3 ] Maior;
[ 4 ] Inserir novos números;
[ 5 ] Sair do programa.''')
op = int(input('Insira o número da opção escolhida: '))

while op == 4:
    num1 = float(input('\nInsira o primeiro número: '))
    num2 = float(input('Insira o segundo número: '))

    print('''Operações disponíveis
    [ 1 ] Somar;
    [ 2 ] Multiplicar;
    [ 3 ] Maior;
    [ 4 ] Inserir novos números;
    [ 5 ] Sair do programa.''')
    op = int(input('Insira o número da opção escolhida: '))

if op == 1:
    total = num1 + num2
    print('A soma dos números inseridos é {:.2f}'.format(total))
elif op == 2:
    total = num1 * num2
    print('A multiplicação dos números inseridos é {:.2f}'.format(total))
elif op == 3:
    if num1 > num2:
        total = num1
        print('O número maior inserido é {:.2f}'.format(total))
    else:
        total = num2
        print('O número maior inserido é {:.2f}'.format(total))
