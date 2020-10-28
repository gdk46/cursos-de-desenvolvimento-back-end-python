import time

frases = ['Carregando.', 'Carregando..', 'Carregando...']

for i in range(0, len(frases)):
    print("\033[K", frases[i].strip(), end="\r")
    
    time.sleep(1) 