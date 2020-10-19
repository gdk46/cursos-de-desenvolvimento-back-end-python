#nome completo
"""  
requisitos
    - interação com o usuario -ok
    - quantas vezes aparece a letra a -ok
    - em que posição ela aparece a primeira vez
    - em que posição ela aparece a última vez
"""

a = str(input("digite uma frase: ")).lower().strip()
a_find = a.find('a') + 1
a_rfind = a.rfind('a') + 1
a_count = a.count('a') 

print("o primeiro 'a' encontrada na posição", a_find)
print("o ultimo 'a' encontrada na posição", a_rfind)
print('existe x de letras "a"', a_count)
