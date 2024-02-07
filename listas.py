# *** CRIANDO UMA LISTA VAZIA ***
lista_de_guiche = []
print(lista_de_guiche)

# *** CRIANDO UMA LISTA COM NÚMERO DE POSIÇÕES E DADOS DEFINIDOS ***
lista_de_guiche = [34949, 34234, 65645, 90905, 34593, "Valores alfanumérico: 123...", True, 10.50]
print(lista_de_guiche)

# *** CRIANDO  UMA LISTA COM UM NÚMERO DE POSIÇÕES DEFINIDAS, MAS SEM DEFINIR OS DADOS QUE IRÃO COMPOR CADA ***
lista_2 =[None]*5
lista_2 [3] = "Rodrigo Mello"
print(lista_de_guiche)

# *** OBTENDO O TAMANHO DE UMA LISTA ***
len(lista_2)

# *** INCLUINDO DADOS EM UMA LISTA ***
lista_2 = []
lista_2.append("Cliente Preferencial")
print(lista_2)

# *** REMOVENDO DADOS EM UMA LISTA ***
print(lista_de_guiche)
lista_de_guiche.remove(90905)
print(lista_de_guiche)

# *** CONCATENANDO DUAS LISTAS ***
lista_2 =[]
lista_2.append("Cliente Preferencial")
lista_2 += lista_de_guiche
print(lista_2)
lista_3 = ["Gestantes", "Idosos"]
lista_2 = lista_2 + lista_3
print(lista_2)

print("Lendo os valores da lista utilizando a keyword range()")
for i in range(0,len(lista_de_guiche)):
    print(lista_de_guiche [i])

lista_de_guiche = [34949, 34234, 65645, 90905, 34593, "Valores alfanumérico: 123...", True, 10.50]
print("Lendo os valores da lista utilizando a keyword in")   
for guiche in lista_de_guiche:
    print(guiche)