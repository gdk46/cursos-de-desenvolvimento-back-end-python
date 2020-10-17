# programa para ler os agulos seno cosseno e tangente
from math import radians, sin, cos, tan, radians
import math
an = float(input('ângulo: '))

print('Seno: {:.2f}'.format(sin(radians(an))))
print('Cosseno: {:.2f}'.format(cos(radians(an))))
print('Tangente: {:.2f}'.format(tan(radians(an))))
