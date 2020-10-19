#nome completo
"""  
requisitos
    - todas letras minúsculas
    - todas letras maiúsculas
    - quantas letras tem sem consiterar os espaços    
    - quantas letras tem o primeiro nome
"""
from os import name


nome = str(input("Qual seu nome completo: ")).strip()
nome_mi = nome.upper()
nome_ma = nome.lower()

nome_spc = nome.title()
nome_spc = nome.replace(" ", "")
nome_len = len(nome_spc)
nome_spl = nome.split()

nome_p_len = len(nome_spl[0])

print("nome em minúsculas: {}".format(nome_mi))
print("nome em maiúsculas: {}".format(nome_ma))
print("Quantidade de letras: {}".format(nome_len))
print("Quantidade de letras no primeiro nome: {}".format(nome_p_len))