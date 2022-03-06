soma_idade = 0
media_idade = 0
maior_idade_h = 0
nome_mais_velho = ''

for c in range(1,5):
    print('-----{}ª PESSOA-----'.fomart(p))
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    genero = str(input('GÊNERO: [F/M]')).strip()
    soma_idade += idade
    if c == 1 and genero in 'Mm':
        maior_idade_h = idade
        nome_mais_velho = nome
    if genero in 'Mm' and idade > maior_idade_h:
        maior_idade_h = idade
        nome_mais_velho = nome

media_idade = soma_idade / 4
print('A MÉDIA DE IDADE DO GRUPO É {} ANOS'.format(media_idade))
print('O HOMEM MAIS VELHO SE CHAMA {} E TEM {} ANOS'.format(maior_idade_h, nome_mais_velho))