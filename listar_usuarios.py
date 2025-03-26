def listar_usuarios(usuarios):  # Função para listar os usuários cadastrados
    # Verifica se a lista de usuários está vazia
    if not usuarios:
        print("\n" + "=" * 40)
        print("       Nenhum usuário cadastrado!")
        print("=" * 40 + "\n")
        return

    # Exibe a lista de usuários cadastrados
    print("\n" + "=" * 40)
    print("       Lista de Usuários Cadastrados")
    print("=" * 40 + "\n")
    for i, usuario in enumerate(usuarios, start=1):
        print(f"Usuário {i}:")
        print(usuario.exibir_dados())  # Chama o método exibir_dados() para cada objeto da classe Usuario
        print("-" * 40)  # Separador entre os usuários
