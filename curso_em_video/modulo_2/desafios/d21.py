"""  
    Analisador completo
    Requisitos:

"""
from time import sleep

entrevista = 0
media_idade = 0
mulheres = 0
nome_mais_velho = ""
idade_mais_velho = 0

for i in range(0,4):
    nome = str(input('seu nome: '))
    idade = int(input('sua idade: '))
    print("""  
        Digite seu sexo biológico:
           [m] - Masculino
           [f] - feminino
    """)
    sexo = str(input('seu sexo biológico: ')).upper()
    sleep(1)


    if sexo == "F" and idade > 20:
        mulheres += 1

    elif sexo == "M" and idade > idade_mais_velho:
        idade_mais_velho = idade
        nome_mais_velho = nome


    media_idade += idade  
    entrevista += 1

media_idade = media_idade / 4
print(""" 
    Analizador completo:
    --------------------------------------------------

    Mulheres com mais de 20 anos: {}
    Homem mais velho do grupo: {} com {} de idade
    Média de idade do grupo: {}
    Total de entrevistas: {}
 """.format(mulheres, nome_mais_velho, idade_mais_velho, media_idade, entrevista))