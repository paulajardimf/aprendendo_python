nome = str(input('Escreva um nome: ')).strip()
print('Analisando o nome...')
print('Nome em letras maiúsculas: {}'.format(nome.upper()))
print('Nome em letras minúsculas: {}'.format(nome.lower()))
print('Quantidade de letras: {}'.format(len(nome) - nome.count(' ')))
print('Quantidade de letras no primeiro nome: {}'.format(nome.find(' ')))
