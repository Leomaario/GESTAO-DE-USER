# CLASSE PARA ARMAZENAR O USUÁRIO """
# USANDO O METODO __INIT__ PARA INICIALIZAR OS ATRIBUTOS """

class Usuario:
    def __init__(self, nome, email, idade):
        self.nome = nome
        self.email = email
        self.idade = idade

    def exibir_dados(self):
        # Retorna a string formatada para que você possa usá-la fora do método
        return f"\nNome: {self.nome}\nEmail: {self.email}\nIdade: {self.idade}\n"

    def __str__(self):
        # Reutiliza o método exibir_dados para a representação como string
        return self.exibir_dados()
