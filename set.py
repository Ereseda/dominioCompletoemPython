# *** TRABALHANDO COM SET(CONJUNTO) ***
# CRIANDO UMA COLLECTION DO TIPO SET
lista_de_clientes_agência_001 = {"Eduardo", "Marcos", "Paulo", "Tatiana", "Jaqueline", "Juliana"}
print(lista_de_clientes_agência_001)

# UNIÃO DOS ELEMENTOS ENTRE DOIS SET
lista_de_clientes_agência_001 = {"Eduardo", "Marcos", "Paulo", "Tatiana", "Jaqueline", "Juliana"}
lista_de_clientes_agência_002 = {"Renato", "Jaqueline", "Eduardo", "Marcelo", "Paulo", "Tatiana"}
print("União entre o set Agência 001 e 002", lista_de_clientes_agência_001.union(lista_de_clientes_agência_002))
print("União entre o set Agência 001 e 002", lista_de_clientes_agência_001 | lista_de_clientes_agência_002)

# IDENTIFICANDO ELEMENTOS COMUNS ENTRE DOIS SETS
lista_de_clientes_agência_001 = {"Eduardo", "Marcos", "Paulo", "Tatiana", "Jaqueline", "Juliana"}
lista_de_clientes_agência_002 = {"Renato", "Jaqueline", "Eduardo", "Marcelo", "Paulo", "Tatiana"}
print("Elementos comuns entre o set Agência 001 e Agência 002 são ", lista_de_clientes_agência_001 & lista_de_clientes_agência_002)
print("Elementos comuns entre o set Agência 001 e Agência 002 são ", lista_de_clientes_agência_001.intersection (lista_de_clientes_agência_002))

# IDENTIFICANDO ELEMENTOS QUE ESTÃO SOMENTE EM UM SET
lista_de_clientes_agência_001 = {"Eduardo", "Marcos", "Paulo", "Tatiana", "Jaqueline", "Juliana"}
lista_de_clientes_agência_002 = {"Renato", "Jaqueline", "Eduardo", "Marcelo", "Paulo", "Tatiana"}
print("Elementos que estão em somente um dos set", lista_de_clientes_agência_001 - lista_de_clientes_agência_002)
print("Elementos que estão em somente um dos set", lista_de_clientes_agência_001.difference( lista_de_clientes_agência_002))

# INCLUINDO OU ATUALIZANDO ELEMENTOS DE UM SET COM OS MÉTODOS ADD() OU UPDATE()
lista_de_clientes_agência_001 = {"Eduardo", "Marcos", "Paulo", "Tatiana", "Jaqueline", "Juliana"}
lista_de_clientes_agência_001.update(("Ricardo", "Regina", "Valter"))
# lista_de_clientes_agência_001.add("Cristina")
print(lista_de_clientes_agência_001)

# REMOVENDO ELEMENTOS DE UM SET COM OS MÉTODOS REMOVE(), DISCARD()OU POP()
print(lista_de_clientes_agência_001)
lista_de_clientes_agência_001.discard("Ricardo")
lista_de_clientes_agência_001.remove("Valter")
lista_de_clientes_agência_001.remove("Regina")

print(lista_de_clientes_agência_001)
lista_de_clientes_agência_001.pop()
print(lista_de_clientes_agência_001)
print(lista_de_clientes_agência_001.pop())
print(lista_de_clientes_agência_001)

# REMOVENDO ELEMENTOS DUPLICADOS DE UM SET
lista_de_clientes = ["Eduardo", "Paulo","Marcos", "Paulo", "Tatiana", "Jaqueline","Eduardo", "Juliana"]
elementos_unicos = set(lista_de_clientes)
print(elementos_unicos)

# DEFININDO UM SET COM ELEMENTOS QUE NÃO PODEM SER MODIFICADOS(FROZEN BASED SETS.)
lista_de_clientes_agência_001 = {"Eduardo", "Marcos", "Paulo", "Tatiana", "Jaqueline", "Juliana"}
lista_de_clientes_agência_003 = frozenset(lista_de_clientes_agência_001)
lista_de_clientes_agência_003.add("João")
print(lista_de_clientes_agência_003)