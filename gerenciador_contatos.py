# O código irá criar um menu de contatos, com a opção de criar, listar ou excluir contatos. Os contatos serão salvos com base no nome e no número de telefone.

contatos = {}

def adicionar_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone: ")
    contatos[nome] = telefone
    print(f"Contato {nome} adicionado com sucesso!")

def ver_contatos():
    if not contatos:
        print("Nenhum contato encontrado.")
        return
    print("\n--- Seus Contatos ---")
    for nome, telefone in contatos.items():
        print(f"Nome: {nome}, Telefone: {telefone}")
    print("-----------------------\n")

def remover_contato():
    nome = input("Digite o nome do contato que deseja remover: ")
    if nome in contatos:
        del contatos[nome]
        print(f"Contato {nome} removido.")
    else:
        print(f"Contato {nome} não encontrado.")

while True:
    print("\n--- Menu de Contatos ---")
    print("1. Adicionar contato")
    print("2. Ver todos os contatos")
    print("3. Remover contato")
    print("4. Sair")
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == '1':
        adicionar_contato()
    elif escolha == '2':
        ver_contatos()
    elif escolha == '3':
        remover_contato()
    elif escolha == '4':
        print("Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")
