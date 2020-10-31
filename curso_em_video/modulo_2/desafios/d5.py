""" 
    Media do aluno
"""
nota1 = float(input('Digite sua nota do primeiro bimestre: '))
nota2 = float(input('Digite sua nota do segubndo bimestre: '))
nota3 = float(input('Digite sua nota do terceiro bimestre: '))
nota4 = float(input('Digite sua nota do quarto bimestre: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media < 5:
    print("Você está reprovado com média {:.2f}".format(media))

elif media > 5 and media < 7:
    print("Você está em recuperação com média {:.2f}".format(media))
elif media >= 7:
    print("Você está aprovado com média {:.2f}".format(media))
