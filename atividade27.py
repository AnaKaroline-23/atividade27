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

usuarios = []

for nomes in range(1,8):
    usuarios.append(str(input("digite o nome dos convidados!  ")))

remover = str(input("Deseja remover algum convidado da lista? (sim/não): "))

if remover == "sim":
    removernome = str(input("digite o nome do convidado a ser removido: "))
    usuarios.remove(removernome)

    print("a lista atualizada com o nome removido é: ", usuarios)

elif remover == "não":
    print("a lista de usuários é: ",usuarios)
