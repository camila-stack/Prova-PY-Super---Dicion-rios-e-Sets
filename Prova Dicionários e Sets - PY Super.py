alunos = {}

while True:
    print()
    print("MENU:")
    print()
    print("OQUE VOCÊ DESEJA FAZER?")
    print("adicionar - Adicionar informações")
    print("remover - Remover informações")
    print("visualizar - Exibir todas as informações")
    print("sair - Fechar e salvar")
    print()
    decisao = input("Digite oque deseja fazer: ")
    print()

    if decisao == "adicionar":
        matricula = int(input("Digite o número da matrícula: "))
        nome = input("Digite o nome do aluno: ")
        alunos[matricula] = nome

    elif decisao == "remover":
        matricula = int(input("Digite o número da matrícula: "))
        nome = input("Digite o nome do aluno: ")
        nome = alunos.pop(matricula)

    elif decisao == "visualizar":
        for chave, valor in alunos.items():
            print(f"{chave}: {valor}")

    elif decisao == "sair":
        break
    