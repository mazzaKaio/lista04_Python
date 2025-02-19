# Faça um programa que solicite ao usuário para digitar seu nome e um número qualquer e em seguida, 
# exiba seu nome várias vezes de acordo com o número digitado.

nome = input("Digite seu nome: ")
num = int(input("Digite um número (inteiro): "))
print("\n")

for i in range(num):
    print(nome)

print("\nFim do programa!")    
print("Kaio Gomes do Nascimento Mazza")