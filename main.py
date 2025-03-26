from cadastrar_usuario import cadastrar_usuario
from listar_usuarios import listar_usuarios
from buscar_usuarios import buscar_usuario_por_nome

usuarios = []  # Lista para armazenar os usuários

while True:  # Menu de opções
    print("\n" + "=" * 40)
    print("      Sistema de Cadastro de Usuários")
    print("=" * 40)
    print("1 - Cadastrar usuário")
    print("2 - Exibir usuários")
    print("3 - Buscar usuário por nome")
    print("4 - Sair")
    print("=" * 40)

    # Solicitação da opção desejada
    opcao = input("Digite a opção desejada: ")

    # Verifica a opção escolhida
    if opcao == "1":
        cadastrar_usuario(usuarios)  # Chamando a função de cadastro
    elif opcao == "2":
        listar_usuarios(usuarios)  # Chamando a função para listar os usuários
    elif opcao == "3":
        nome = input("Digite o nome do usuário que deseja buscar: ")
        usuario_encontrado = buscar_usuario_por_nome(usuarios, nome)
        if usuario_encontrado:
            print(f"\nUsuário encontrado:\n{usuario_encontrado}")
        else:
            print("\nUsuário não encontrado!")
    elif opcao == "4":
        print("\nSaindo do sistema...")  # Encerrando o programa
        break
    else:
        print("\nOpção inválida! Por favor, selecione uma opção válida.")
