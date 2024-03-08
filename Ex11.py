#  11. Faça um programa que receba o salário de um funcionário. Calcule e imprima o valor do novo salário, sabendo que ele recebeu um aumento de 21,37 %.

print("Salario inicial:")
salInicial = float(input())
aumento = 1.2137
salFinal = salInicial * aumento

print(f'o salario final é igual a: {salFinal:.2f}')