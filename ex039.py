from datetime import date

nascimento = int(input('Insira o ano de nascimento: '))
ano_atual = date.today().year

if ano_atual - nascimento < 18:
    print('Ainda não chegou a hora de se alistar, faltam {} anos.'.format(18-(ano_atual - nascimento)))
elif ano_atual - nascimento > 18:
    print('Já passou {} anos do prazo de se alistar.'.format(18-(ano_atual - nascimento)))
else:
    print('Você completou {} anos, está na hora de se alistar.'.format(ano_atual - nascimento))
