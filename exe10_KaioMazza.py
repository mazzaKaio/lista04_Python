"""
Faça um programa que pergunte quantas pessoas o usuário deseja convidar para uma festa.
- Se ele digitar um número abaixo de 10, peça os nomes e após cada nome exiba a mensagem: "[nome] está convidado para a festa". 
- Se ele inserir um número 10 ou superior, exiba a mensagem "Muitas pessoas".
"""

numPessoas = int(input("Digite o número de pessoas que você quer convidar para a festa: "))

if numPessoas < 10:
    for i in range(numPessoas):
        convidado = input("\nDigite o nome do {}º convidado: ".format(i+1))
        print("{} está convidado para a festa!".format(convidado))
else:
    print("Muitas pessoas! (cuidado com a aglomeração!)")

print("\nFim do programa!")
print("Kaio Gomes do Nascimento Mazza")