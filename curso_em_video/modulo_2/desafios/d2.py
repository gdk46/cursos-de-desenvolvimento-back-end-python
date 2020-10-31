""" 
    Mostrar a base de conversão
    Requisitos
    o usuario deve escolher a a base de conversão do sistema
    0 - binario
    1 - octal
    2 - hexadecimal
"""
num = int(input('Digite um número: '))
print("""  
Conveta o numero para uma das opções abaixo
    0 - binario
    1 - octal
    2 - hexadecimal
""")
escolha = float(input('Escolha uma opção: '))

if escolha == 0:
    print("Número em binario: {}".format(bin(num)))


elif escolha == 1:
    print("Número em octal: {}".format(oct(num)))


elif escolha == 2:
    print("Número em hexadecimal: {}".format(hex(num)))


else:
    print("Erro")