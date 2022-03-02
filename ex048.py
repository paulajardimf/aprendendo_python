#soma entre todos os números ímpares que são múltiplos de 3
#e que se encontram no intervalo entre 1 até 500
num = int(0)

for c in range(1,500+1):
    if not c % 2 == 0:
        if c % 3 == 0:
            print(c)
            num = num + c
print(num)

