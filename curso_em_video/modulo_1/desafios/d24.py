#nome completo
"""  
requisitos
    - de 0 a 9999 mostrar cada digito separador    
"""

numero = str(input("digite um numero de 0 a 9999: "))
unidade = numero[0:1]
dezena = numero[1:2]
centena = numero[2:3]
milhar = numero[3:]

print('unidade: {}, dezena: {}, centena: {}, milhar: {}'.format(unidade, dezena, centena, milhar))