# 15. Leia um valor inteiro positivo em segundos, e imprima-o em horas, minutos e segundos.

print("Escreva um numero inteiro e positivo:", end=" ")
segundos = int(input())

horas = segundos // 3600 
segundos %= 3600
minutos = segundos // 60
segundos %= 60

print(f"{horas} hora(s), {minutos} minuto(s), {segundos} segundo(s).")