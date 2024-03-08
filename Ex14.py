# Leia um número inteiro de 4 dígitos (de 1000 a 9999) e imprima 1 dígito por linha.

print("Numero de 4 digitos:")
number = int(input())

primeiroDigito = number // 1000
segundoDigito = (number // 100) % 10
terceiroDigito = (number // 10) % 10
quartoDigito = number % 10

print(primeiroDigito)
print(segundoDigito)
print(terceiroDigito)
print(quartoDigito)