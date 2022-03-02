from datetime import date

nascimento = int(input('Insira o ano de nascimento do(a) atleta: '))
ano_atual = date.today().year
idade = ano_atual - nascimento

if idade <= 9:
    print('O(A) atleta tem {} anos, e está na categoria MIRIM.'.format(idade))
elif idade > 9 and idade <= 14:
    print('O(A) atleta tem {} anos, e está na categoria INFANTIL.'.format(idade))
elif idade > 14 and idade <= 19:
    print('O(A) atleta tem {} anos, e está na categoria JUNIOR.'.format(idade))
elif idade == 20:
    print('O(A) atleta tem {} anos, e está na categoria SÊNIOR.'.format(idade))
else: print('O(A) atleta tem {} anos, e está na categoria MASTER.'.format(idade))
