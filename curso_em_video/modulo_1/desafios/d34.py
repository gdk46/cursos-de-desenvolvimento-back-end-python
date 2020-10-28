import emojis

val_user = float(input('digite o valor do seu salário : '))
salario = 1250.00

if  salario <= val_user:
    procentagem = 10
    """ 
        1250 - 100
        125  -  10        
    """
    valor_total = salario + ((val_user * procentagem) / 100)

    print("""
        O valor da viagem é de {}
    """.format(valor_total))

elif salario > val_user:
    procentagem = 15
    """ 
        1250 - 100
        125  -  15        
    """
    valor_total = salario + ((val_user * procentagem) / 100)


    print("""  
        O valor da viagem é de {}
    """.format(valor_total))

else:
    print('Erro')

