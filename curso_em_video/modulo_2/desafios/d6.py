""" 
    Categária do atleta
"""
from datetime import date


nacimento = int(input('Digite o ano de seu nascimento: '))
idade = date.today().year - nacimento

if idade <= 9:
    print("Mirin")

elif idade >= 9 and idade <= 14:
    print("Infantil")

elif idade >= 14 and idade <= 19:
    print("Junior")

elif idade >= 20:
    print("Master")
