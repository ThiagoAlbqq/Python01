#  8. Leia uma velocidade em km/h (quilômetros por hora) e apresente-a convertida em m/s (metros por segundo). A fórmula de conversão é: M = K/3.6 , sendo K a velocidade em km/h e M em m/s.

print("Qual a valocidade em km/h:")
km = float(input())

mPerSeconds = km/3.6

print(f'a velocidade em metros por segundo é igual a: {mPerSeconds:.2f}')