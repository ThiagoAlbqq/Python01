#  7. Faça um programa que leia a temperatura em graus Celsius e converta para Fahrenheit. Fórmula: F = C * (9.0/5.0) + 32.

print("Graus celsius:")
celsius= float(input())

fahrenheit = celsius * (9/5) + 32

print(f'Fahrenheit: {fahrenheit:.2f}')