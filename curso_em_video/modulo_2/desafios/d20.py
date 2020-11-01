"""  
    Maior e menor da sequência
"""
maior_peso = 0
menor_peso = 0
for i in range(0,4):
    peso = float(input('Digite o peso: '))
    
    if i == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
                
        if peso < menor_peso:
            menor_peso = peso

print(""" 
    Analizador De peso:
    -------------------------
    Maior peso no grupo: {}
    Menor peso no grupo: {}
 """.format(maior_peso, menor_peso))