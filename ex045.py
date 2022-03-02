from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')

print('_=_'*13)
print('ESCOLHA ENTRE PEDRA, PAPEL OU TESOURA ')
print('_=_'*13)
print('''[  0  ] PEDRA
[  1  ] PAPEL
[  2  ] TESOURA''')
pessoa = int(input('SUA ESCOLHA: '))
maquina = randint(0,2)

print('P E D R A')
sleep(1)
print('P A P E L')
sleep(1)
print('T E S O U R A')
sleep(1)

print('_=_'*13)
print('O computador escolheu {}'.format(itens[maquina]))
print('Você escolheu {}'.format(itens[pessoa]))
print('_=_'*13)

if maquina == 0: #pedra
    if pessoa == 0:
        print('EMPATE!')
    elif pessoa == 1:
        print('VENCEU MISERÁVI!!!')
    elif pessoa == 2:
        print('ERROOOUU!!!')
    else: print('JOGADA INVÁLIDA')

elif maquina == 1: #papel
    if pessoa == 0:
        print('ERROOOUU!!!')
    elif pessoa == 1:
        print('EMPATE!')
    elif pessoa == 2:
        print('VENCEU MISERÁVI!!!')
    else: print('JOGADA INVÁLIDA')

elif maquina == 2: #tesoura
    if pessoa == 0:
        print('VENCEU MISERÁVI!!!')
    elif pessoa == 1:
        print('ERROOOUU!!!')
    elif pessoa == 2:
        print('EMPATE!')
    else: print('JOGADA INVÁLIDA')

print('_=_'*13)