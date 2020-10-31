""" 
    compra no cartão
"""

compra = int(input('Digite valor da compra: '))

print("""  
compra deve ser paga com:
    0 - cartão/cheque - 10%
    1 - a vista no cartão - 5%
    2 - parcelado
""")
pagamento = float(input('Escolha uma opção: '))


if pagamento == 0:
    valoCompra = compra - (compra * 10) / 100
    print("valor da compra: {}".format(valoCompra))


elif pagamento == 1:
    valoCompra = compra - ((compra * 5) / 100)
    print("valor da compra: {}".format(valoCompra))


elif pagamento == 2:
    print("""  
    Parcelas:
            0 - não parcelado até 2X
            1 - parcelado 3X ou mais
    """)
    parcela = float(input('Escolha uma opção: '))
    
    if parcela == 0:
        print("valor da compra: {}".format(compra))
    
    elif parcela == 1:
        valoCompra = compra - ((compra * 20) / 100)
        print("valor da compra: {}".format(valoCompra))

else:
    print("Erro")