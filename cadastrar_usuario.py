from usuario import Usuario  # IMPORTANDO A CLASSE USUARIO DO ARQUIVO usuario.py

# FUNÇÃO PARA CADASTRAR UM USUÁRIO E ADICIONAR NA LISTA DE USUÁRIOS
def cadastrar_usuario(usuarios):
    print("\n" + "=" * 40)
    print("       Cadastro de Novo Usuário")
    print("=" * 40)

    # Validação do nome (não pode ser número e não pode estar vazio)
    while True:
        nome = input("Digite o nome do usuário: ").strip()
        if nome.isdigit():
            print("Erro: O nome não pode ser um número. Tente novamente.")
        elif not nome:
            print("Erro: O nome não pode estar vazio. Tente novamente.")
        else:
            break  # Nome válido

    # Validação do e-mail (verifica se contém '@' como uma validação simples)
    while True:
        email = input("Digite o email do usuário: ").strip()
        if '@' not in email:
            print("Erro: O e-mail deve conter o caractere '@'. Tente novamente.")
        elif not email:
            print("Erro: O e-mail não pode estar vazio. Tente novamente.")
        else:
            break  # E-mail válido

    # Validação da idade (deve ser um número válido)
    while True:
        idade = input("Digite a idade do usuário: ").strip()
        if not idade.isdigit():  # Verifica se é um número
            print("Erro: A idade deve ser um número válido. Tente novamente.")
        else:
            idade = int(idade)
            break  # Idade válida

    # Cria o usuário como um objeto da classe Usuario e adiciona à lista
    novo_usuario = Usuario(nome, email, idade)
    usuarios.append(novo_usuario)

    print("\n" + "=" * 40)
    print("Usuário cadastrado com sucesso!")
    print("=" * 40)
