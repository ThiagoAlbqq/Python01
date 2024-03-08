# 2. Faça um programa que, a partir das medidas dos lados de um retângulo, lidos via teclado, calcule a área e o perímetro deste retângulo.

# Qual a espressão da area de um retangulo
# A = b.h
# Qual a espressão do perimetro de um retangulo
# P = 2b + 2h

print("Qual a base do retangulo?")
base = float(input())
print("Qual a altura do retangulo?")
altura = float(input())

# Variaveis fixas
area = base * altura
perimetro = (2*base) + (2*altura)

print(f'a area do retangulo é igual a: {area:.2f}')
print(f'a perimetro do retangulo é igual a: {perimetro:.2f}')
