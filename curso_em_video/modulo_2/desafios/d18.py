"""  
    Detector de Palíndromo		
    Requisitos:

"""

frase = str(input("digite uma frase: ")).strip().upper()
palavra = frase.split()
joing = ''.join(palavra)
inversu = joing[::-1]

print('inverso {}'.format(inversu))


# 
if inversu == joing:
    print('uma descoberta!! essa palavra é um Palíndromo')
else:
    print('essa palavra não é um Palíndromo')