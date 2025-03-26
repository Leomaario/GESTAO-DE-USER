# Sistema de Cadastro de Usuários

Este é um sistema simples de cadastro de usuários desenvolvido em Python. Ele permite o cadastro, listagem e busca de usuários, além de realizar validações para garantir a integridade dos dados inseridos.

## Funcionalidades

- **Cadastro de Usuários**: Permite cadastrar um usuário fornecendo nome, e-mail e idade. O sistema valida os dados de entrada.
- **Listagem de Usuários**: Exibe todos os usuários cadastrados com suas informações (nome, e-mail e idade).
- **Busca de Usuários**: Permite buscar usuários pelo nome e exibir suas informações.

## Estrutura do Projeto

O projeto está dividido em três arquivos principais:

### 1. `usuario.py`
Contém a definição da classe `Usuario`, que representa um usuário com as informações de nome, email e idade. A classe possui um método `exibir_dados` para exibir os dados do usuário.

### 2. `listar_usuarios.py`
Contém as funções para:
- **Listar usuários**: Exibe todos os usuários cadastrados.
- **Buscar usuário por nome**: Permite buscar e exibir os dados de um usuário pelo nome fornecido.

### 3. `main.py`
Arquivo principal que interage com o usuário e permite que ele escolha entre cadastrar, listar ou buscar um usuário. Contém o fluxo principal do programa.
