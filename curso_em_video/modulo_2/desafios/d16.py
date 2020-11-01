"""  
    Progressão Aritimétrica
    Requisitos:

"""
a = int(input('termo: '))
b = int(input('razão: '))
c = a + (20 - 1) * b
for i in range(a, c, b):
    print("{}=> ".format(i), end='')
    if i >= 20:
        print("babouuuu ", end=':)')