# Peça ao usuário para inserir um número que deseja a tabuada e em seguida inserir a tabuada conforme o número digitado.

num = int(input("Digite o número que você deseja consultar a tabuada: "))

for i in range(11):
    resultado = num * i
    print("{} x {} = {}".format(num, i, resultado))

print("Kaio Gomes do Nascimento Mazza")