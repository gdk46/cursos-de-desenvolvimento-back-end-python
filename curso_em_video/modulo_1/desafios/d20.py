# faça um programa que sortei a ordem de apresentação de cada grupo 
# e apresente o nome do grupo e a ordem de apresentação
import random
from random import shuffle

a1 = str(input("aluno 1: "))
a2 = str(input("aluno 2: "))
a3 = str(input("aluno 3: "))
a4 = str(input("aluno 4: "))
a5 = str(input("aluno 5: "))
a6 = str(input("aluno 6: "))


Aluno = [a1, a2, a3, a4, a5, a6]
shuffle(Aluno)

print("=============================")
print("A ordem de LINDEZA da família:")
print(Aluno)