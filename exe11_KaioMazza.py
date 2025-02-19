"""
Você é um desenvolvedor de sistemas trabalhando em um projeto colaborativo com sua equipe.
Para garantir que todas as tarefas do projeto sejam concluídas dentro do prazo, você decide criar um pequeno programa para controlar o status das tarefas.
O programa deve permitir que você insira o nome de cada tarefa e indique se ela está concluída ou não.
No final, o programa deve apresentar um resumo com o total de tarefas, quantas estão concluídas e quantas ainda estão pendentes.
Desenvolva um programa em Python que:
1.	Solicite ao usuário o número de tarefas a serem inseridas.
2.	Para cada tarefa, solicite o nome da tarefa e se ela está concluída (aceitando "sim", "s", "não" ou "n").
3.	Conte e exiba o número de tarefas concluídas e não concluídas.
"""

numTarefas = int(input("Digite o número de tarefas que você deseja inserir: "))
tarefas = []
statusTarefas = []
tarefasConcluidas = 0
tarefasNaoC = 0

for i in range(numTarefas):
    nomeTarefa = input("\nDigite o nome da {}ª tarefa: ".format(i+1))
    isConcluida = input("Digite se ela está concluída [sim/s, nao/n]: ").lower()

    tarefas.append(nomeTarefa)
    statusTarefas.append(isConcluida)

for tarefa in statusTarefas:
    if tarefa[0] == "s":
        tarefasConcluidas +=1
    elif tarefa[0] == "n":
        tarefasNaoC += 1
    
print("\nTarefas adicionadas: {}\nTarefas concluidas: {}\nTarefas não concluidas: {}".format(len(tarefas), tarefasConcluidas, tarefasNaoC))

print("\nFim do programa!")
print("Kaio Gomes do Nascimento Mazza")