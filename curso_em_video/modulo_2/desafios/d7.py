""" 
    IMC
"""

weight = input('Qual seu pesso? ')
height = input('Qual sua altura? ')
height_total = float(height) * float(height)
imc = float(weight) / height_total

if imc <= 18.5:
    print('seu imc é de {:.2f} e você está abaixo do peso'.format(imc))

elif imc >= 18.5 and imc <= 25:
    print('seu imc é de {:.2f} e você está com peso ideal'.format(imc))

elif imc >= 25 and imc <= 30:
    print('seu imc é de {:.2f} e você está com sobrepeso'.format(imc))

elif imc >= 30 and imc <=40:
    print('seu imc é de {:.2f} e você está com obsidade'.format(imc))

elif imc >= 40:
    print('seu imc é de {:.2f} e você está com obsidade móbida'.format(imc))