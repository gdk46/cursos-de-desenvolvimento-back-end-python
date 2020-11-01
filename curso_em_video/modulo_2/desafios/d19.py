"""  
    Grupo da Maioridade
    Requisitos:

"""
maior = 0
menor = 0
entrevista = 0
for i in range(0,6):
    p = int(input('sua idade: '))

    if p >= 21:
        maior +=1
    else:
        menor +=1

    entrevista +=1

print('Pessoas maiores de idade {}, pessoas menores de idade {}, total de pessoas intrevistada: {}'.format(maior, menor, entrevista))