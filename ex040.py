n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))

media = (n1 + n2) / 2
print('Sua média é {:.1f}'.format(media))

if media < 5.0:
    print('REPROVADO')
elif media >= 5.0 and media <= 6.9:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')
