# Peça ao usuário para inserir seu nome e um número. 
# Se o número for menor do que 10 (num < 10), exiba o nome dele esse número de vezes, 
# caso contrário, exiba a mensagem “Número muito alto!” três vezes.

nome = input("Digite seu nome: ")
num = int(input("Digite um número: "))

if num < 10:
    for i in range(num):
        print(nome)
else:
    for i in range(3):
        print("Número muito alto!")