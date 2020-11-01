"""  
    Soma de pares
    Requisitos:

"""
n = int(input('Digite um número: '))

if n % 2 == 0 or n % 3 == 0:
    for soma in range(1, n):
        somando = soma + n       
        print("{} + {} = {}".format(soma, n, somando))
