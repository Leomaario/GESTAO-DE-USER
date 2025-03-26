from usuario import Usuario
from listar_usuarios import listar_usuarios

# Função para buscar usuário por nome
def buscar_usuario_por_nome(usuarios, nome):
    print("\n" + "=" * 40)
    print("       Busca de Usuário")
    print("=" * 40)

    for usuario in usuarios:  # Percorre a lista de objetos Usuario
        if usuario.nome.lower() == nome.lower():  # Comparação sem case-sensitive
            print("\n" + "=" * 40)
            print("Usuário encontrado!")
            print("=" * 40)
            print(usuario.exibir_dados())  # Exibe os dados do usuário encontrado
            return usuario  # Retorna o objeto Usuario

    # Caso o usuário não seja encontrado
    print("\n" + "=" * 40)
    print("Usuário não encontrado!")
    print("=" * 40)
    return None  # Retorna None explicitamente
