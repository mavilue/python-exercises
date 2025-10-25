# cadastrar nome e matricula de discentes

def cadastrar_discente():
    nome = input("Digite o nome do aluno: ")
    matricula = int(input("Digite o número da matrícula: "))

    with open("discente.txt","a") as arquivo:
        arquivo.write(f"Aluno(a): {nome} | Matrícula: {matricula}\n")
    print("Cadastro feito com sucesso!")

def listar_dados():
    print("Lista de todos os alunos cadastrados:")
    with open("discente.txt","r") as arquivo:
        s = arquivo.readlines()
        for i in s:
            print(i.strip())

def menu():

    while True:
        print("=== ESCOLHA UMA DAS OPÇÕES ===")
        print("1. Cadastrar discente")
        print("2. Listar discentes")
        print("3. Sair")

        opc = input("Escolha uma opção: ")

        if opc=="3":
            break

        elif opc=="1":
            print()
            cadastrar_discente()
        elif opc=="2":
            print()
            listar_dados()
        else:
            print("Opção errada! Tente novamente!")
        print()

menu()