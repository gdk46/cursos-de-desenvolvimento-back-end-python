
"""     
    "impar ou par" não levando em cota algumas regras da matemática
    para fazer essa classificação. 
"""
import emojis

val = int(input('Digite um número: '))
resto_d = val % 2


if resto_d == 0:
    print('par')    
else:
    print('impar')
    