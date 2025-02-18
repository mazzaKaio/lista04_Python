# Peça um número abaixo de 50 e em seguida, faça uma contagem regressiva de 50 até esse número, 
# certificando-se de mostrar o número inserido na saída.

num = int(input("Digite um número ABAIXO DE 50: "))

if num < 50:
    for i in range(50, num - 1, -1):
        print(i)
else:
    print("Número digitado maior do que 50!")

print("\nFim do programa!")    
print("Kaio Gomes do Nascimento Mazza")