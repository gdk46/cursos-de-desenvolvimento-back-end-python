""" 
    Pocketown
"""

from random import choice
import emojis


print(emojis.encode("""  
    1 - :punch: - pedra
    2 - :raised_hand: - papel
    3 - :v: - tesoura
"""))


user = int(input('escolha: '))
lista = [1,2,3]
pocketown = {1: ':punch:', 2: ':raised_hand:', 3: ':v:'}
listType = {1: 'pedra', 2: 'papel', 3: 'tesoura'}
valueList = choice(lista)


if user <= 0 and user > 3:
    print('digite um número correto:')
    
else:
    if user == valueList:
        print("==== VOCÊ EMPATOU ====")
        print("\033[1;34m", "VOCÊ", emojis.encode(pocketown[user]), emojis.encode(listType[user]))
        print("\033[1;34m", "MÁQUINA", emojis.encode(pocketown[valueList]), emojis.encode(listType[user]))
        
    elif user < valueList:
        print("==== VOCÊ PERDEU ====")
        print("\033[1;31m", "VOCÊ", emojis.encode(pocketown[user]), emojis.encode(listType[user]))
        print("\033[1;31m", "MÁQUINA", emojis.encode(pocketown[valueList]), emojis.encode(listType[user]))

    elif user > valueList:
        print("==== VOCÊ GANHOU ====")
        print("\033[0;32m", "VOCÊ", emojis.encode(pocketown[user]), emojis.encode(listType[user]))
        print("\033[0;32m", "MÁQUINA", emojis.encode(pocketown[valueList]), emojis.encode(listType[valueList]))
        