# Conteúdo dos enunciados
enunciados = [
    """# Crie um programa que permita fazer a conversão cambial entre Dólares e Reais. Considere como taxa de câmbio US$ 1,00 = R$5,27. Leia um valor em Dólares pelo teclado e mostre o correspondente em Reais.""",
    """# Faça um programa que, a partir das medidas dos lados de um retângulo, lidos via teclado, calcule a área e o perímetro deste retângulo.""",
    """# Leia um número inteiro e imprima o seu antecessor e o seu sucessor.""",
    """# Leia o tamanho do lado de um quadrado e imprima como resultado a sua área.""",
    """# Elaborar um programa para calcular e imprimir o volume (V) de uma esfera e a área (A) de sua superfície, dado o valor de seu raio (R). A fórmula do volume da esfera é V = 4/3 πR3 e A = 4πR2 .""",
    """# Faça um programa que leia um número real e imprima o resultado do quadrado desse número.""",
    """# Faça um programa que leia a temperatura em graus Celsius e converta para Fahrenheit. Fórmula: F = C * (9.0/5.0) + 32.""",
    """# Leia uma velocidade em km/h (quilômetros por hora) e apresente-a convertida em m/s (metros por segundo). A fórmula de conversão é: M = K/3.6 , sendo K a velocidade em km/h e M em m/s.""",
    """# Leia um ângulo em graus e apresente-o convertido em radianos. A fórmula de conversão é: R = G * π/180 , sendo G o ângulo em graus e R em radianos.""",
    """# Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos três valores e o quadrado da soma dos três valores.""",
    """# Faça um programa que receba o salário de um funcionário. Calcule e imprima o valor do novo salário, sabendo que ele recebeu um aumento de 21,37 %.""",
    """# Faça um programa que receba um valor em R$ que será dividido entre três ganhadores de um concurso. Sendo que da quantia total: ◦ O primeiro ganhador receberá 46%; ◦ O segundo ganhador receberá 32%; ◦ O terceiro receberá o restante; Calcule e imprima a quantia ganha por cada um dos ganhadores.""",
    """# Faça um programa que leia um número inteiro positivo de três dígitos (de 100 a 999). Gere outro número formado pelos dígitos invertidos do número lido. Exemplo: Número Lido = 123, Número Gerado = 321.""",
    """# Leia um número inteiro de 4 dígitos (de 1000 a 9999) e imprima 1 dígito por linha.""",
    """# Leia um valor inteiro positivo em segundos, e imprima-o em horas, minutos e segundos.""",
    """# Escreva um programa que leia as coordenadas x e y de pontos no R2 e calcule sua distância da origem (0, 0).""",
    """# Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido proporcionalmente ao valor que cada deu para a realização da aposta. Faça um programa que leia quanto cada apostador investiu, o valor do prêmio, e imprima quanto cada um ganharia do prêmio com base no valor investido.""",
    """# Escreva um programa que receba como entrada o valor do saque realizado pelo cliente de um banco e retorne quantas notas de cada valor serão necessárias para atender ao saque com a menor quantidade de notas possível. Serão utilizadas notas de 100, 50, 20, 10, 5, 2 e 1 real.""",
    """# Faça um programa que leia uma string e então a imprima.""",
    """# Crie um programa que calcula o comprimento de uma string.""",
    """# Faça um programa que leia um nome e imprima as 4 primeiras letras do nome.""",
    """# Escreva um programa que recebe uma string S e inteiros não-negativos I e J e imprima o segmento S[I…J].""",
    """# Leia uma cadeia de caracteres e converta todos os caracteres para maiúscula.""",
    """# Escreva um programa para converter uma cadeia de caracteres de letras maiúsculas em letras minúsculas.""",
    """# Leia uma string contendo letras de uma frase, inclusive os espaços em branco. Retirar os espaços em branco e depois escrever a frase resultante.""",
    """# Faça um programa em que troque todas as ocorrências de uma letra L1 pela letra L2 em uma string. A string e as letras L1 e L2 devem ser fornecidas pelo usuário.""",
    """# Escreva um programa que recebe do usuário uma string S, um caractere C, e uma posição I.""",
    """# Construa um programa que leia duas strings fornecidas pelo usuário e verifique se a segunda string lida está contida no final da primeira, retornando o resultado da verificação"""
]

# Loop para criar os arquivos
for i, enunciado in enumerate(enunciados, start=1):
    nome_arquivo = f"Ex{i}.py"
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(enunciado)
    print(f"Arquivo '{nome_arquivo}' criado com sucesso.")