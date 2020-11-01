"""  
    Contagem regressiva
    Requisitos:
        pausa de 1 segundo 
"""
from time import sleep
from emojis import encode

fogo_artificio = encode(""":collision::collision::collision::collision::collision::collision::collision::collision:""")

for estoura in range(10, 0, -1):
    print(estoura)
    sleep(1)

    if estoura == 1:
        print("Feliz ano novo!")
        print(fogo_artificio)
