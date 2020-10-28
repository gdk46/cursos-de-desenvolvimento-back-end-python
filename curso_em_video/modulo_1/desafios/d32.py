import emojis


distancia = 200
val_user = float(input('quantos KM foi percorrido: '))


if  distancia >= val_user:
    valor_viagem = 0.50
    valor_total = val_user * valor_viagem

    print("""  
        O valor da viagem é de {}
    """.format(valor_total))

elif distancia < val_user:
    valor_viagem = 0.45
    valor_total = val_user * valor_viagem


    print("""  
        O valor da viagem é de {}
    """.format(valor_total))

else:
    print('Erro')

