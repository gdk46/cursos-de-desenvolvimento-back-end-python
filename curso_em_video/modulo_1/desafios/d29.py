""" 
    Requisistos:
    var inteiro = com um número já definido de 0 a 5
    interação com o usuário
    notíciar a vitória com msg na tela
"""
from random import randint
import emojis, random


int_number = randint(0, 5)
val_user = int(input('Digite um número de 0 a 5: '))

if val_user == int_number:    
    print(
        emojis.encode("""  
        Párabens Você ganhou do nosso sistema Nª{} :clap::ghost::slot_machine:
    """).format(int_number))
elif val_user > 5 or val_user < 0:
    print(
        emojis.encode("""  
        o número que você digitou não é permitido :sob::sob:
    """))

else:
    print(
        emojis.encode("""  
        Nosso sistema ganhou de você Nª{} :fire::alien:
    """).format(int_number))
    

