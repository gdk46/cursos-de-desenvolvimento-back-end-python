"""  
    Soma impares múltiplos de 3
    Requisitos:

"""
n_contagem = 500
soma = 0
total = 0

for contagem in range(0, n_contagem + 1):
    
    if contagem % 2 == 1 or contagem % 3 == 1:
        soma += contagem
        print('O entre o {} total: {}'.format(contagem, soma))
