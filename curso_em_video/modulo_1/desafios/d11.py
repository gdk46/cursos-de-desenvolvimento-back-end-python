#pinta a parede 
#calcular a area da parede sendo que a paraede tem x larfura e y altura
#cada litro de tinta pinda uma area de 2m² (dois metros quadrados)
#quantos litros de tinta vou precisar

areaB = float(input('digite o largura da parede do seu quarto: '))
areaH = float(input('digite o altura da parede do seu quarto: '))
a = (areaB * areaH) / 2

print('Você precisa de {:.0f} latas de tinta'.format(a))
