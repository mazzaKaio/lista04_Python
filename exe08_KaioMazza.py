"""
Defina uma variável chamada “total” como 0 (total = 0). 
Peça ao usuário para inserir 5 números e após cada entrada, pergunte se ele deseja que este número seja incluído (‘S’ ou ‘s’, ‘N’ ou ‘n’).
Se ele desejar, adicione o número ao total e se ele não quiser inclui-lo, não adicione. Depois de inserir os 5 números, exiba o total.
"""

total = 0

for i in range(5):
    num = int(input("\nDigite o {}º número: ".format(i + 1)))
    resposta = input("Você deseja incluir este número no total [s/n]: ").upper()

    if resposta.__eq__("S"):
        total += num

print("\nTotal da soma: {}".format(total))

print("\nFim do programa!")    
print("Kaio Gomes do Nascimento Mazza")