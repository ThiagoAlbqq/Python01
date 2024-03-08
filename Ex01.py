# 1. Crie um programa que permita fazer a conversão cambial entre Dólares e Reais. Considere como taxa de câmbio US$ 1,00 = R$5,27. Leia um valor em Dólares pelo teclado e mostre o correspondente em Reais.
#Talvez o end dificulte a aprovação do teste

print("Digite um valor:", end=" ")
real = float(input())
dol = float(5.27)

conversor = real * dol

print(f' R$ {conversor:.2f}')