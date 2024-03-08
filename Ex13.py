# Faça um programa que leia um número inteiro positivo de três dígitos (de 100 a 999). Gere 
# outro número formado pelos dígitos invertidos do número lido. Exemplo: Número Lido = 
# 123, Número Gerado = 321.

print("Numero de 3 digitos:")
number = int(input())

primeiroDigito = number // 100
segundoDigito = (number // 10) % 10
terceiroDigito = number % 10
print(f'Aqui está a inversão do numero: {terceiroDigito}{segundoDigito}{primeiroDigito}')