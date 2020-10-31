""" 
    maior de dois numeros
"""
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))


if num1 > num2:
    print("O maio é: {}, o menor é: {}".format(num1, num2))
elif num1 < num2:
    print("O maio é: {}, o menor é: {}".format(num2, num1))
elif num1 == num2:
    print("Ambos são iguais")
else:
    print('erro')