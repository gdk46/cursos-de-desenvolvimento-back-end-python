""" 
    Alistamento
    se for maio de 18 pode se alisatar
"""

idade = int(input('qual sua idade? '))
if idade < 18:
    tempo = 18 - idade 
    print('Você não tem idade para alistar somente daqui à {}'.format(tempo))
elif idade == 18:
    print('Você deve se alistar')
elif idade > 18:
    tempo = idade - 18 
    print('Você já passou da idade de se alistar à {}'.format(tempo))
else:
    print('Erro')