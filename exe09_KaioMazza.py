"""
Faça um programa que pergunte em qual direção o usuário deseja contar (para cima = c, para baixo = a). 
•	Se ele selecionar para cima, peça um número superior e conte de 1 até o número digitado. 
•	Se ele selecionar para baixo, peça um número abaixo de 20 e em seguida faça a contagem regressiva de 20 até o número digitado.
•	Se ele inserir algo diferente do pedido, insira uma mensagem “Direção inválida!”
"""

direcaoDesejada = input("Insira qual direção você deseja, cima(c) ou abaixo(a): ").lower()

if direcaoDesejada[0].__eq__("c"):
    num = int(input("Digite um número inteiro: "))

    print("\nContagem:")
    for i in range(num):
        print(i + 1)

elif direcaoDesejada[0].__eq__("a"):
    num = int(input("Digite um número ABAIXO de 20: "))
    if num <= 20:
    
    else:
        print("Número inserido não é menor do que 20!")