

while True:
    num = (int(input('Insira um número para visualizar a sua tabuada: ')))
    for c in range(1,11):
        print(f'{c:2} X {num} = {c * num}')
    if num < 0:
        break