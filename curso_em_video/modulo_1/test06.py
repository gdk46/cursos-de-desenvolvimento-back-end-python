tempo = int(input('Quantos anos tem seu carro: '))



if tempo <= 3:
    print("Seu carro está novo")
else:
    print("está na hora de trocar esse possante!")


#   if simplificado, python não tem operador ternário
print('----- Condiçãos simplificada -----')
a = 'carro novo' if tempo <= 3 else 'Carro velho'
print(a)
