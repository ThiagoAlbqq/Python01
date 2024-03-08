# 9. Leia um ângulo em graus e apresente-o convertido em radianos. A fórmula de conversão é: R = G * π/180 , sendo G o ângulo em graus e R em radianos.
import math

print("Qual a angulo em graus?")
anguloG = float(input())

anguloR = anguloG * (math.pi/180)

print(f'o angulo em radianos é igual a: {anguloR:.2f}')