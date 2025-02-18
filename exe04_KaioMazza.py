# Escreva um programa para pedir um número e em seguida o nome. 
# Exiba o nome (uma letra de cada vez em cada linha) e repita isso para o número de vezes que ele digitou.

nome = input("Digite seu nome: ")
num = int(input("Digite um número: "))

for i in range(num):
    print("\n")
    for x in range(len(nome)):
        print(nome[x])
    
print("Kaio Gomes do Nascimento Mazza")