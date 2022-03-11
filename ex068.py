#par ou impar
from random import randint

print('---JOGO PAR OU IMPAR---\n')

while True:
    num_maq = randint(0, 5)
    escolha = str(input('Par ou Impar? [ Digite P ou I ]: ')).upper().split()
    num_pessoa = int (input('Digite um número de 0 a 5: '))
    par_impar = (num_maq + num_pessoa) % 2

    if par_impar == 0 and escolha == 'P':
        print(f'O Computador escolheu o número {num_maq}')
        print('VOCÊ GANHOU!!!')
        break
    elif par_impar != 0 and escolha == 'I':
        print(f'O Computador escolheu o número {num_maq}')
        print('VOCÊ GANHOU!!!')
        break
    else:
        print(f'O Computador escolheu o número {num_maq}')
        print('Tente novamente.')
