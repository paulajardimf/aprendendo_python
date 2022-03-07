genero = str(input('Digite seu gênero [F/M]: ')).strip.upper()[0]

while genero != 'F' or genero != 'M':
    print('CARACTERE INCORRETO, DIGITE NOVAMENTE.')
    genero = str(input('Digite seu gênero [F/M]: ')).upper()
