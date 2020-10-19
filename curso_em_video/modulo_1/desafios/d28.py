nome_c = str(input("digite seu nome: ")).strip()
nome = nome_c.split()
print('primeiro nome {} ultimo nome {}'.format(nome[0], nome[len(nome) - 1]))