# ninja das strings
from os import replace


x = "Curso de Desenvolvimento Python no curso em video"
y = """Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    Duis consectetur lectus in eleifend pretium.
    Vivamus fringilla consequat tortor. Maecenas et maximus nulla.
    Sed eget nisi sit amet ante imperdiet elementum quis ut nisi."""



tamanho = len(x)
local_palavra = x.find('Desenvolvimento')
palavra_1 = x[9:]
palavra_2 = x[9:25]
palavra_3 = x[::3]


x = x.replace("Curso de", "cusando")
print(x)
x = x.capitalize()
print(x)

vogal_em_y = y.count('e')
#print(vogal_em_y)

