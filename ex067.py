

while True:
    num = (int(input('Insira um número para visualizar a sua tabuada: ')))
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{c:2} X {num} = {c * num}')
print('Programa encerrado.')