#o professor que sortear um de seus 4 alunos para apagar o quadro
# sistema de sorteio

from random import choice
from emoji import emojize


a1 = str(input("aluno 1: "))
a2 = str(input("aluno 2: "))
a3 = str(input("aluno 3: "))
a4 = str(input("aluno 4: "))

arrAluno = [a1, a2, a3, a4]
escolido = choice(arrAluno)
print(emojize('o aluno escolhido foi o {} :it:'.format(escolido)))