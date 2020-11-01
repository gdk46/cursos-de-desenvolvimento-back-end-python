"""  
    Contagem de pares
    Requisitos:
        um numero para ser par tem que ser divisivel por mais de 2 divisores
"""
n_contagem = 50
for contagem in range(0, n_contagem + 1):
    
    if contagem % 2 == 0 or contagem % 3 == 0:
        print('O número {} é par'.format(contagem))



