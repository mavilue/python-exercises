def calcular_media(notas):
    return sum(notas) / len(notas)


alunos = []

while True:
    nome = input("Digite o nome do aluno: ")
    notas = []
    for i in range(1, 4):
        nota = float(input(f"Nota {i}: "))
        notas.append(nota)

    media = calcular_media(notas)

    if media >= 6:
        status = "Aprovado"
    elif media >= 4:
        status = "Recuperação"
    else:
        status = "Reprovado"

    alunos.append({
        "nome": nome,
        "notas": notas,
        "media": media,
        "status": status
    })

    cont = input("Deseja adicionar outro aluno? (s/n): ").lower()
    if cont != 's':
        break

# Relatório final
print("\n--- RESULTADO FINAL ---")

# Inicializa maior e menor com a média do primeiro aluno
maior = alunos[0]['media']
menor = alunos[0]['media']

aprovados = recuperacao = reprovados = 0

for aluno in alunos:
    print(f"{aluno['nome']}: média {aluno['media']:.1f} → {aluno['status']}")

    # Atualiza maior e menor média
    if aluno['media'] > maior:
        maior = aluno['media']
    if aluno['media'] < menor:
        menor = aluno['media']

    # Conta status
    if aluno['status'] == "Aprovado":
        aprovados += 1
    elif aluno['status'] == "Recuperação":
        recuperacao += 1
    else:
        reprovados += 1

print(f"\nAlunos cadastrados: {len(alunos)}")
print(f"Aprovados: {aprovados}")
print(f"Recuperação: {recuperacao}")
print(f"Reprovados: {reprovados}")
print(f"Maior média: {maior}")
print(f"Menor média: {menor}")