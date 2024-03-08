# Faça um programa que receba um valor em R$ que será dividido entre três ganhadores de 
# um concurso. Sendo que da quantia total:
#  ◦ O primeiro ganhador receberá 46%;
#  ◦ O segundo ganhador receberá 32%;
#  ◦ O terceiro receberá o restante;
# Calcule e imprima a quantia ganha por cada um dos ganhadores.

print("Valor total")
total = float(input())

ganhador1 = total * 0.46
ganhador2 = total * 0.32
ganhador3 = total * 0.22

print(f'O premio para o ganhador 1 é igual a: {ganhador1:.2f}')
print(f'O premio para o ganhador 2 é igual a: {ganhador2:.2f}')
print(f'O premio para o ganhador 3 é igual a: {ganhador3:.2f}')