"""  
    Números primos
"""

n = int(input('Digite um número: '))
tot = 0
for i in range(1, n):
    if n % i == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')

print(tot)