# 10. Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos três valores e o quadrado da soma dos três valores.

print("Valor 1?")
v1 = float(input())
print("Valor 2?")
v2 = float(input())
print("Valor 3?")
v3 = float(input())

somaQuadrados = v1 ** 2 + v2 ** 2 + v3 ** 2
quadradoDaSoma = (v1 + v2 + v3) ** 2

print(f'a soma dos quadrados dos três valores é igual a: {somaQuadrados:.2f}')
print(f'o quadrado da soma dos três valores é igual a: {quadradoDaSoma:.2f}')