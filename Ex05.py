# 5. Elaborar um programa para calcular e imprimir o volume (V) de uma esfera e a área (A) de sua superfície, dado o valor de seu raio (R). A fórmula do volume da esfera é V = 4/3 πR3 e A = 4πR2 .
import math

print("Indique o raio:", end=" ")
raio = float(input())

volume = (4/3) * math.pi * raio ** 3
area = 4 * math.pi * raio ** 2

# Valores aproximados
print(f'Volume {volume:.2f}')
print(f'Area {area:.2f}')