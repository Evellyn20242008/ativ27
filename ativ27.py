# Solicite ao usuário que insira o nome de até 7 convidados.
# Armazene os nomes em uma lista.
# Permita ao usuário remover um convidado da lista, caso necessário.
# Exiba a lista final de convidados.

# Digite o nome do convidado 1: João
# Digite o nome do convidado 2: Maria
# ...
# Digite o nome do convidado 7: Pedro
# Deseja remover algum convidado da lista? (sim/não): sim
# Digite o nome do convidado a ser removido: Maria
convidados = []

# Loop para receber os nomes dos convidados
for i in range(7):
    nome = input(f"Digite o nome do convidado {i + 1}: ")
    convidados.append(nome)

# Pergunta se deseja remover algum convidado
remover = input("Deseja remover algum convidado da lista? (sim/não): ").strip().lower()

if remover == 'sim':
    nome_remover = input("Digite o nome do convidado a ser removido: ")
    if nome_remover in convidados:
        convidados.remove(nome_remover)
        print(f"{nome_remover} foi removido da lista.")
    else:
        print(f"{nome_remover} não está na lista.")

# Exibe a lista final de convidados
print("Lista final de convidados:")
for convidado in convidados:
    print(convidado)