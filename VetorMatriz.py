alunos = ["alice","bruno", "carla"]

dias = ["seg", "ter", "qua", "qui"]

reservas = [["Ausente" for _ in dias] for _ in alunos]

print("preencha com 'S' para presença e 'X' para ausência:")

for i, aluna in enumerate(alunos):
    print(f"\naluno: {aluno}")
    for j, dia in enumerate(dias):
        entrada = input(f" {dia}: ")
        if entrada.upper() == 'S':
            reservas[i][j] = "Presente"

print("\nTabela de reserva:")
print(f"{'aluna':<10} {' '.join( [f'{d:<10}' for d in dias])}")
for i, aluno in enumerate(alunos):
    print(f"{aluno:<10} {' '.join([f'{res:<10}' for res in reservas[i]])}")