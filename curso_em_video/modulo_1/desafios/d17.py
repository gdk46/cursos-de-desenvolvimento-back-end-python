# faça um programa que leia o cateto oposto e do catedo adjacente
# de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
from math import hypot

'''
    o ² da hipotenusa é igual aos catetos adjacentes ou seja 
    a² = b² + c² 
'''
print('===================== cálcule a hipotenusa  =====================')
b = float(input('comprimento do cateto oposto: '))
c = float(input('comprimento do cateto adjacente: '))
# a = (b**2 + c**2) ** (1/2)
# print('hipotenusa equivale: {}'.format(a))

print('hipotenusa equivale: {}'.format(hypot(b, c)))