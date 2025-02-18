# Faça um programa que solicite ao usuário para digitar seu nome e um número qualquer e em seguida, 
# exiba seu nome várias vezes de acordo com o número digitado.

nome = input("Digite seu nome: ")
num = int(input("Digite um número (inteiro): "))

for i in range(num):
    print(nome)

print("Kaio Gomes do Nascimento Mazza")