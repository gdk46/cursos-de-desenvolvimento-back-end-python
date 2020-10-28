a = float(input("1ª segmento: "))
b = float(input("2ª segmento: "))
c = float(input("3ª segmento: "))

if a < b + c and b < a + c and c < a + b:
    print('o segmento acima pode formar um triângulo')
else:
    print('o segmento acima não pode formar um triângulo')