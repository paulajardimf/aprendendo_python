#palíndromo

print('Verificador de Palíndromo')
frase = str(input('Insira a frase e/ou palavra: ')).strip().upper()
letras = frase.split()
junto = ''.join(letras)

print('Você digitou a frase {}'.format(junto))

inverso = ''

for letra in range (len(junto) - 1, -1, -1):
    inverso += junto [letra]
print(junto, inverso)

if inverso == junto:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')
