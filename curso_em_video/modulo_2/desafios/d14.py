"""  
    Taboada
    Requisitos:

"""
n = int(input('Escolha um número para fazer a taboada até o dez, digite aqui: '))

for x in range(1, 11):
    print('{} X {} = {}'.format(n, x, n * x))
