#número primo
num = int(input('Digite um número: '))
total = 0

for c in range (1, num +1):
    if num % c == 0:
        print('\033[34m', end=" ")
        total += 1
    else:
        print('\033[m', end=" ")
    print('{}'.format(c), end=" ")

print('\n\033[mO número {} foi divisível por {} vezes.'.format(num, total))

if total == 2:
    print('Por isso ele é primo.')
else:
    print('Por isso ele não é primo.')