"""
Você é um desenvolvedor de sistemas trabalhando em um projeto para um salão de beleza. O salão precisa de um sistema para gerenciar os horários de atendimento dos clientes. 
Primeiro, a dona do salão monta a grade horária da agenda. Depois, uma cliente deseja agendar um horário, e o sistema exibe os horários disponíveis. 
A dona do salão então agenda o horário escolhido pela cliente, e o horário escolhido não estará mais disponível. 
O sistema deve continuar permitindo agendamentos até que todos os horários disponíveis sejam preenchidos ou até que a dona do salão decida parar.
Desenvolva um programa em Python que:
1.	Solicite à dona do salão para inserir os horários disponíveis na agenda.
2.	Exiba os horários disponíveis para a cliente.
3.	Permita que a cliente escolha um horário para agendamento.
4.	Atualize a agenda marcando o horário escolhido como ocupado.
5.	Pergunte se deseja agendar mais um horário e continue até que todos os horários estejam preenchidos ou a dona do salão decida parar.
"""

horariosDisponiveis = []

qntHorarios = int(input("Digite quantos horarios voce tem disponivel: "))

for i in range(qntHorarios):
    horario = input("Digite o {}º horario [HH:MM]: ".format(i+1))
    horariosDisponiveis.append(horario)

print("\n----Área da cliente:")
for i in range(qntHorarios):
    print("Horários disponiveis: {}".format(horariosDisponiveis))
    horarioDesejado = input("\nDigite o horário que você deseja [HH:MM]: ")
    try:
        verificacao = horariosDisponiveis.index(horarioDesejado)
    except:
        print("\nHorário '{}' não encontrado ou digitado errado!".format(horarioDesejado))
        continue

    horariosDisponiveis.remove(horarioDesejado)
    print("\n{} foi agendado com sucesso!".format(horarioDesejado))

    confirmacao = input("Você deseja agendar outro horario [sim/s, nao/n]? ").lower()

    if confirmacao[0].__eq__("n"):
        print("\nEncerrando programa...")
        break